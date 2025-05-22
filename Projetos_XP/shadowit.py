# -*- coding: utf-8 -*-
from flask import Blueprint
from .logger import init_log
import click
from .jobs import create_job
from .mongo import mongo_sgs
from .. import app
from .splunk import search
import pandas as pd
import numpy as np
from bson import ObjectId
import re 
import datetime, time
bp = Blueprint('shadowit', __name__)
logger = init_log("shadowit", app.config['LOG_LEVEL_SHADOWIT'])


def mongo_recriar_collection(collection, df):

    """
    Insere um DataFrame do pandas em uma coleção do MongoDB.

    :param collection: A coleção do MongoDB onde os documentos serão inseridos.
    :param df: DataFrame do pandas contendo os dados.
    :return: Mensagem de sucesso no log.
    """
    # delete colecttion 
    mongo_sgs[collection].delete_many({})

    documentos = df.to_dict(orient="records")  # Converte DataFrame em lista de dicionários
    if not documentos:
        logger.info('O Dataframe está vázio. Nenhum documento foi insertido')
        return
    mongo_sgs[collection].insert_many(documentos)  # Insere todos os documentos de uma vez
    return logger.info(f'Collection: {collection} preenchida com {len(documentos)} documentos.')

def mongo_insert_collection(collection, df):
    """
    Insere um DataFrame do pandas em uma coleção do MongoDB.

    :param collection: A coleção do MongoDB onde os documentos serão inseridos.
    :param df: DataFrame do pandas contendo os dados.
    :return: Mensagem de sucesso no log.
    """
    documentos = df.to_dict(orient="records")  # Converte DataFrame em lista de dicionários
    if not documentos:
        logger.info('O Dataframe está vázio. Nenhum documento foi insertido')
        return
    mongo_sgs[collection].insert_many(documentos)  # Insere todos os documentos de uma vez
    return logger.info(f'Collection: {collection} preenchida com {len(documentos)} documentos.')


def search_hierarquia_usuario(df, by_field):
    df_spl = df
    
    if by_field == 'mail':

        lista = df_spl['id_usuario'].tolist()
        lista_unic = list(set(lista))
        lista_resultado = []
        registro_encontrado = mongo_sgs.databricks_share_gente_organograma.find({"mail": {"$in":lista_unic}})
        if registro_encontrado:
            for row in list(registro_encontrado):
                lista_resultado.append(row)
        else: 
            lista_resultado = mongo_sgs.databricks_share_gente_organograma.find_one()

        return pd.DataFrame(lista_resultado)
    
    if by_field == 'id':

        # Cruzar email (ldap_users) com email (databricks_share_gente_organograma)
        # Fazer lista de e-mails que os ID's que batem.
        lista_id = df_spl['id_account'].tolist()
        lista_unic_id = list(set(tuple(item) if isinstance(item, list) else item for item in lista_id))
        lista_resultado_id = []
        registro_encontrado_id = mongo_sgs.ldap_users.find({"sAMAccountName": {"$in":lista_unic_id}})
        if registro_encontrado_id:
            for row in tuple(registro_encontrado_id):
                lista_resultado_id.append(row)
        else: 
            lista_resultado_id = mongo_sgs.ldap_users.find_one()

        registros_emails = pd.DataFrame(lista_resultado_id)
        registros_emails = registros_emails.rename(columns={'mail':'id_usuario'})
        registros_emails = registros_emails[['id_usuario']].astype(str)     

        return registros_emails

def search_aval (df):
    df_spl = df
    lista = df_spl['nm_aplicacao'].tolist()
    lista_unic = list(set(lista))
    lista_resultado = []
    registro_encontrado = list(mongo_sgs.netskope_apps.find({"nameService": {"$in": lista_unic}}))
    
    if registro_encontrado:
        for row in registro_encontrado:
            lista_resultado.append(row)
        
    else:
        lista_resultado = mongo_sgs.netskope_apps.find().limit(1)

    df = pd.DataFrame(lista_resultado)
    df = df[['nameService','nr_avaliacao','origem_aval','is_shadowit','jarvix_comment']]        
    return df

def search_excecoes_netskope(df):
    df_spl = df
    registro_encontrado = list(mongo_sgs.netskope_categorias.find())

    lista_resultado = []
    if registro_encontrado:
        for row in registro_encontrado:
            lista_resultado.append(row['name'])
    
    lista_resultado.append('Categorias_Permitidas_High') 
    lista_resultado.append('Categorias_Permitidas_Low')
    lista_resultado.append('URL_Exceção_Categoria')   
    df_spl['fl_categoria_excecao'] = df_spl['nm_categoria_aplicacao'].apply(lambda x:  1 if any(nm_categoria_aplicacao in str(x) for nm_categoria_aplicacao in lista_resultado) else 0)

    return df_spl



def search_grupo_excecoes_netskope(df):
    df_spl = df
    lista_resultado = []
    df_spl['fl_categoria_excecao_grupo'] = df_spl['nm_grupo_regra_risco'].astype(str).str.contains(r'App_', na=False).astype(int)

    return df_spl

def search_criterio_shadowit(tp_shadowit):
    registro_encontrado = list(mongo_sgs.shadowit_criterio_peso.find({"tp_shadowit": tp_shadowit}))
    lista_resultado = []
    if registro_encontrado:
        for row in registro_encontrado:
            lista_resultado.append(row)

    return pd.DataFrame(lista_resultado)

# Criar uma função para classificar a confiança
def classificar_confianca(cci):
    if 0 <= cci <= 25:
        return 'Baixa'
    elif 26 <= cci <= 50:
        return 'Moderada'
    elif 51 <= cci <= 75:
        return 'Alta'
    elif 76 <= cci <= 100:
        return 'Muito Alta'
    else:
        return 'Desconhecido'

@bp.cli.command('saas') 
def saas():
    job_objectid, job = create_job("shadowit_saas", None, None, None)        
    try:


        logger.info('Lendo SPL da view shadowit_regras') 
        view = mongo_sgs.shadowit_regras.find_one({'title':'shadowit_saas'})
        view_spl = view['spl']
        view_earliest_time = view['earliest_time']
        result = search(view_spl,view_earliest_time)

        logger.info('transformando resultado em DataFrame Pandas') 
        df_spl = pd.DataFrame(result['results'])
        df_spl = df_spl[['dt_evento','id_usuario', 'nm_categoria_aplicacao','tp_action','nm_dominio_aplicacao','nm_url_completo','vl_cci_score','qt_acesso_realizados','nm_aplicacao','nm_grupo_regra_risco']]
        

        logger.info('procurando excecoes') 
        df_spl= search_excecoes_netskope(df_spl)
        df_spl= search_grupo_excecoes_netskope(df_spl)

        logger.info('procurando avaliacoes') 
        df_aval = search_aval(df_spl)
        logger.info('gravando tabela df_aval_teste')
    
        
        logger.info('procurando hierarquia')  
        df_hierarquia = search_hierarquia_usuario(df_spl)
        df_hierarquia = df_hierarquia [['nome','mail','n1','n2','n3','squad']].rename(columns={'nome':'nm_usuario','mail':'id_usario_hierarquia','n1':'nm_gestao_n1','n2':'nm_gestao_n2','n3':'nm_gestao_n3','squad':'nm_area'})

        logger.info('realizando joins')   
        df_shadowit_hierarquia = pd.merge(df_spl, df_hierarquia,left_on = 'id_usuario' , right_on = 'id_usario_hierarquia', how = 'left')
        df_shadowit_aval = pd.merge(df_shadowit_hierarquia, df_aval, left_on = 'nm_aplicacao' , right_on = 'nameService', how = 'left')
    
        
        logger.info('criando campos de flag para Criterios') 
        df_shadowit_criterios = df_shadowit_aval
        df_shadowit_criterios['tp_shadowit_tb'] = 'SaaS'
        df_shadowit_criterios['fl_categoria_bloqueadas'] = np.where(df_shadowit_criterios['nm_categoria_aplicacao'].astype(str).str.contains('Categorias_Bloqueadas', case=False, na=False),1,0)
        df_shadowit_criterios['fl_aval'] = np.where((df_shadowit_criterios['nr_avaliacao'].isna()) | (df_shadowit_criterios['nr_avaliacao']== '-') ,1,0)
        df_shadowit_criterios['fl_categoria_shadowit'] = np.where(df_shadowit_criterios['nm_categoria_aplicacao'].astype(str).str.contains('Categorias_ShadowIT', case=False, na=False) ,1,0)
        df_shadowit_criterios['fl_categoria_excecao'] = np.where((df_shadowit_criterios['fl_categoria_excecao']==1) | (df_shadowit_criterios['fl_categoria_excecao_grupo'] == 1),1,0)
        df_shadowit_criterios['fl_is_shadowit'] = np.where(df_shadowit_criterios['is_shadowit']== 'Sim',1, 0)
        df_shadowit_criterios['fl_match_nestskope_apps'] = np.where((df_shadowit_criterios['is_shadowit']== 'Sim')|(df_shadowit_criterios['is_shadowit']== 'Não'),1, 0)

        #Classificar a confianca
        df_shadowit_criterios['vl_cci_score'] = pd.to_numeric(df_shadowit_criterios['vl_cci_score'], errors='coerce')
        #Aplicar a função ao DataFrame
        df_shadowit_criterios['tp_classificacao_cci'] = df_shadowit_criterios['vl_cci_score'].apply(classificar_confianca)
    
        logger.info('criando os critérios Shadowit') 
        df_criterios_shadowit = search_criterio_shadowit('saas')
        df_criterios_shadowit_1 = df_criterios_shadowit[df_criterios_shadowit['id']==1]
        df_criterios_shadowit_2 = df_criterios_shadowit[df_criterios_shadowit['id']==2]
        df_criterios_shadowit_3 = df_criterios_shadowit[df_criterios_shadowit['id']==3]
        df_criterios_shadowit_4 = df_criterios_shadowit[df_criterios_shadowit['id']==4]
        df_criterios_shadowit_5 = df_criterios_shadowit[df_criterios_shadowit['id']==5]
        df_criterios_shadowit_6 = df_criterios_shadowit[df_criterios_shadowit['id']==6]

        logger.info('aplicando critérios Shadowit 1: ind_criterio_blaklist') 
        df_shadowit = pd.merge(df_shadowit_criterios, df_criterios_shadowit_1, left_on = 'tp_shadowit_tb' , right_on = 'tp_shadowit', how = 'left')
        df_shadowit['ind_criterio_blaklist'] = np.where(df_shadowit['fl_categoria_bloqueadas']==1, df_criterios_shadowit_1['Peso'], 0)
        df_shadowit = df_shadowit.drop(columns = ['_id','tp_shadowit','id','Indicador','Peso'])

        logger.info('Aplicando critérios Shadowit 2: ind_criterio_aval') 
        df_shadowit = pd.merge(df_shadowit, df_criterios_shadowit_2, left_on = 'tp_shadowit_tb' , right_on = 'tp_shadowit', how = 'left')
        df_shadowit['ind_criterio_aval'] = np.where(df_shadowit['fl_aval']==1, df_criterios_shadowit_2['Peso'], 0)
        df_shadowit = df_shadowit.drop(columns = ['_id','tp_shadowit','id','Indicador','Peso'])

        logger.info('Aplicando critérios Shadowit 3: ind_criterio_categoria_shadowit ') 
        df_shadowit = pd.merge(df_shadowit, df_criterios_shadowit_3, left_on = 'tp_shadowit_tb' , right_on = 'tp_shadowit', how = 'left')
        df_shadowit['ind_criterio_categoria_shadowit'] = np.where(df_shadowit['fl_categoria_shadowit']==1, df_criterios_shadowit_3['Peso'], 0)
        df_shadowit = df_shadowit.drop(columns = ['_id','tp_shadowit','id','Indicador','Peso'])
        
        logger.info('Aplicando critérios Shadowit 4: ind_criterio_whithlist' ) 
        df_shadowit = pd.merge(df_shadowit, df_criterios_shadowit_4, left_on = 'tp_shadowit_tb' , right_on = 'tp_shadowit', how = 'left')
        df_shadowit['ind_criterio_whithlist'] = np.where(df_shadowit['fl_categoria_excecao']==1, 0, df_criterios_shadowit_4['Peso'])
        df_shadowit = df_shadowit.drop(columns = ['_id','tp_shadowit','id','Indicador','Peso'])

        logger.info('Aplicando critérios Shadowit 5: ind_criterio_cloud_confidence_high') 
        df_shadowit = pd.merge(df_shadowit, df_criterios_shadowit_5, left_on = 'tp_shadowit_tb' , right_on = 'tp_shadowit', how = 'left')
        df_shadowit['ind_criterio_cloud_confidence_high'] = np.where(df_shadowit['vl_cci_score']>=51, 0,df_criterios_shadowit_5['Peso'])
        df_shadowit = df_shadowit.drop(columns = ['_id','tp_shadowit','id','Indicador','Peso'])
        
        logger.info('Aplicando critérios Shadowit 6: ind_criterio_categoria_shadowit_jarvix') 
        df_shadowit = pd.merge(df_shadowit, df_criterios_shadowit_6, left_on = 'tp_shadowit_tb' , right_on = 'tp_shadowit', how = 'left')
        df_shadowit['ind_criterio_categoria_shadowit_jarvix'] = np.where(df_shadowit['fl_is_shadowit']==1, df_criterios_shadowit_6['Peso'], 0)
        df_shadowit = df_shadowit.drop(columns = ['_id','tp_shadowit','id','Indicador','Peso'])

        logger.info('Aplicando critério Shadowit final') 
        df_shadowit['vl_criterio_shadowit'] = df_shadowit['ind_criterio_blaklist'] + df_shadowit['ind_criterio_aval'] + df_shadowit['ind_criterio_categoria_shadowit'] + df_shadowit['ind_criterio_categoria_shadowit_jarvix'] + df_shadowit['ind_criterio_whithlist'] + df_shadowit['ind_criterio_cloud_confidence_high']
        df_shadowit['ind_criterio_shadowit'] = np.where(df_shadowit['vl_criterio_shadowit']>=7,1, 0)

        df_shadowit['dt_execucao_sgs'] = datetime.datetime.now()
        df_shadowit = df_shadowit.fillna("-")
        

        logger.info('Gravando na collection shadowit_saas') 
        df_shadowit_resumo = df_shadowit[(df_shadowit['ind_criterio_shadowit']==1)]
        df_shadowit_resumo = df_shadowit_resumo[['tp_shadowit_tb','dt_evento','nm_aplicacao','nm_url_completo','qt_acesso_realizados',
                                        'id_usuario','nm_usuario', 'id_usario_hierarquia','nm_gestao_n1','nm_gestao_n2','nm_gestao_n3','nm_area',
                                        'tp_classificacao_cci',
                                        'ind_criterio_blaklist','ind_criterio_aval','ind_criterio_categoria_shadowit','ind_criterio_whithlist','ind_criterio_cloud_confidence_high',
                                        'is_shadowit','jarvix_comment','fl_match_nestskope_apps',
                                        'vl_criterio_shadowit','ind_criterio_shadowit',
                                        'nm_categoria_aplicacao','nm_grupo_regra_risco','dt_execucao_sgs']]

        mongo_insert_collection('shadowit_saas',df_shadowit_resumo)

        # descomentar para
        # logger.info('Gravando na collection shadowit_saas_homologacao para homologacao')
        # df_shadowit1 = df_shadowit[(df_shadowit['ind_criterio_shadowit']==1)].fillna("-")
        # mongo_insert_collection('shadowit_saas_homologacao',df_shadowit1)

        # logger.info('Gravando na collection shadowit_saas_homologacao_0 para contra prova')
        # df_shadowit0 = df_shadowit[df_shadowit['ind_criterio_shadowit']==0].fillna("-")
        # mongo_recriar_collection('shadowit_saas_homologacao_0',df_shadowit0)
        nr_linhas = df_shadowit_resumo.shape[0]
        job["total"] = nr_linhas
        logger.info('Fim')
    except Exception as inst:
        job['details']['erro'] = inst
        job["end"] = datetime.datetime.now()
        logger.error("Job {} finalizado Total: {} Erros: {}".format(job_objectid, job["total"], job["error"]))
        mongo_sgs.jobs.update_one({"_id": job_objectid}, {"$set": job}) 

    job["end"] = datetime.datetime.now()
    logger.info("Job {} finalizado Total: {} Erros: {}".format(job_objectid, job["total"], job["error"]))
    mongo_sgs.jobs.update_one({"_id": job_objectid}, {"$set": job})         


@bp.cli.command('api_externa') 
def api_externa():
    job_objectid, job = create_job("shadowit_api_externa", None, None, None)        
    try:


        logger.info('Lendo SPL da view shadowir_regras') 
        view = mongo_sgs.shadowit_regras.find_one({'title':'shadowit_apiexterna'})
        view_spl = view['spl']
        view_earliest_time = view['earliest_time']
        result = search(view_spl,view_earliest_time) #passar via paramentro do view no SPL campo recorrencia
        
        logger.info('Transformando resultado em DataFrame Pandas') 
        df_spl = pd.DataFrame(result['results'])
        df_spl = df_spl[['dt_evento','id_usuario', 'nm_categoria_aplicacao','tp_action','nm_dominio_aplicacao','nm_url_completo','vl_cci_score','qt_acesso_realizados','nm_aplicacao','nm_grupo_regra_risco']]

        logger.info('Procurando excecoes')  
        df_spl= search_excecoes_netskope(df_spl)
        df_spl= search_grupo_excecoes_netskope(df_spl)

        logger.info('Procurando avaliacoes') 
        df_aval = search_aval(df_spl)
        

        logger.info('Procurando hierarquia')  
        df_hierarquia = search_hierarquia_usuario(df_spl)
        df_hierarquia = df_hierarquia [['nome','mail','n1','n2','n3','squad']].rename(columns={'nome':'nm_usuario','mail':'id_usario_hierarquia','n1':'nm_gestao_n1','n2':'nm_gestao_n2','n3':'nm_gestao_n3','squad':'nm_area'})

        logger.info('Realizando joins')   
        df_shadowit_hierarquia = pd.merge(df_spl, df_hierarquia,left_on = 'id_usuario' , right_on = 'id_usario_hierarquia', how = 'left')
        df_shadowit_aval = pd.merge(df_shadowit_hierarquia, df_aval, left_on = 'nm_aplicacao' , right_on = 'nameService', how = 'left')
    
        logger.info('criando campos de flag para Criterios') 
        df_shadowit_criterios = df_shadowit_aval
        df_shadowit_criterios['tp_shadowit_tb'] = 'api_externa'
        df_shadowit_criterios['fl_categoria_bloqueadas'] = np.where(df_shadowit_criterios['nm_categoria_aplicacao'].astype(str).str.contains('Categorias_Bloqueadas', case=False, na=False),1,0)
        df_shadowit_criterios['fl_aval'] = np.where((df_shadowit_criterios['nr_avaliacao'].isna()) | (df_shadowit_criterios['nr_avaliacao']== '-') ,1,0)
        df_shadowit_criterios['fl_categoria_shadowit'] = np.where(df_shadowit_criterios['nm_categoria_aplicacao'].astype(str).str.contains('Categorias_ShadowIT', case=False, na=False) ,1,0)
        df_shadowit_criterios['fl_categoria_excecao'] = np.where((df_shadowit_criterios['fl_categoria_excecao']==1) | (df_shadowit_criterios['fl_categoria_excecao_grupo'] == 1),1,0)
        df_shadowit_criterios['fl_is_shadowit'] = np.where(df_shadowit_criterios['is_shadowit']== 'Sim',1, 0)
        df_shadowit_criterios['fl_match_nestskope_apps'] = np.where((df_shadowit_criterios['is_shadowit']== 'Sim')|(df_shadowit_criterios['is_shadowit']== 'Não'),1, 0)

        df_shadowit_criterios['vl_cci_score'] = pd.to_numeric(df_shadowit_criterios['vl_cci_score'], errors='coerce')

        # Aplicar a função ao DataFrame
        df_shadowit_criterios['tp_classificacao_cci'] = df_shadowit_criterios['vl_cci_score'].apply(classificar_confianca)
    
    
        logger.info('Criando os critérios Shadowit') 
        df_criterios_shadowit = search_criterio_shadowit('api_externa')
        df_criterios_shadowit_1 = df_criterios_shadowit[df_criterios_shadowit['id']==1]
        df_criterios_shadowit_2 = df_criterios_shadowit[df_criterios_shadowit['id']==2]
        df_criterios_shadowit_3 = df_criterios_shadowit[df_criterios_shadowit['id']==3]
        df_criterios_shadowit_4 = df_criterios_shadowit[df_criterios_shadowit['id']==4]
        df_criterios_shadowit_5 = df_criterios_shadowit[df_criterios_shadowit['id']==5]
        df_criterios_shadowit_6 = df_criterios_shadowit[df_criterios_shadowit['id']==6]

        logger.info('aplicando critérios Shadowit 1: ind_criterio_blaklist') 
        df_shadowit = pd.merge(df_shadowit_criterios, df_criterios_shadowit_1, left_on = 'tp_shadowit_tb' , right_on = 'tp_shadowit', how = 'left')
        df_shadowit['ind_criterio_blaklist'] = np.where(df_shadowit['fl_categoria_bloqueadas']==1, df_criterios_shadowit_1['Peso'], 0)
        df_shadowit = df_shadowit.drop(columns = ['_id','tp_shadowit','id','Indicador','Peso'])

        logger.info('Aplicando critérios Shadowit 2: ind_criterio_aval') 
        df_shadowit = pd.merge(df_shadowit, df_criterios_shadowit_2, left_on = 'tp_shadowit_tb' , right_on = 'tp_shadowit', how = 'left')
        df_shadowit['ind_criterio_aval'] = np.where(df_shadowit['fl_aval']==1, df_criterios_shadowit_2['Peso'], 0)
        df_shadowit = df_shadowit.drop(columns = ['_id','tp_shadowit','id','Indicador','Peso'])

        logger.info('Aplicando critérios Shadowit 3: ind_criterio_categoria_shadowit ') 
        df_shadowit = pd.merge(df_shadowit, df_criterios_shadowit_3, left_on = 'tp_shadowit_tb' , right_on = 'tp_shadowit', how = 'left')
        df_shadowit['ind_criterio_categoria_shadowit'] = np.where(df_shadowit['fl_categoria_shadowit']==1, df_criterios_shadowit_3['Peso'], 0)
        df_shadowit = df_shadowit.drop(columns = ['_id','tp_shadowit','id','Indicador','Peso'])
        
        logger.info('Aplicando critérios Shadowit 4: ind_criterio_whithlist' ) 
        df_shadowit = pd.merge(df_shadowit, df_criterios_shadowit_4, left_on = 'tp_shadowit_tb' , right_on = 'tp_shadowit', how = 'left')
        df_shadowit['ind_criterio_whithlist'] = np.where(df_shadowit['fl_categoria_excecao']==1, 0, df_criterios_shadowit_4['Peso'])
        df_shadowit = df_shadowit.drop(columns = ['_id','tp_shadowit','id','Indicador','Peso'])

        logger.info('Aplicando critérios Shadowit 5: ind_criterio_cloud_confidence_high') 
        df_shadowit = pd.merge(df_shadowit, df_criterios_shadowit_5, left_on = 'tp_shadowit_tb' , right_on = 'tp_shadowit', how = 'left')
        df_shadowit['ind_criterio_cloud_confidence_high'] = np.where(df_shadowit['vl_cci_score']>=51, 0,df_criterios_shadowit_5['Peso'])
        df_shadowit = df_shadowit.drop(columns = ['_id','tp_shadowit','id','Indicador','Peso'])
        
        logger.info('Aplicando critérios Shadowit 6: ind_criterio_categoria_shadowit_jarvix') 
        df_shadowit = pd.merge(df_shadowit, df_criterios_shadowit_6, left_on = 'tp_shadowit_tb' , right_on = 'tp_shadowit', how = 'left')
        df_shadowit['ind_criterio_categoria_shadowit_jarvix'] = np.where(df_shadowit['fl_is_shadowit']==1, df_criterios_shadowit_6['Peso'], 0)
        df_shadowit = df_shadowit.drop(columns = ['_id','tp_shadowit','id','Indicador','Peso'])

        logger.info('Aplicando critério Shadowit final') 
        df_shadowit['vl_criterio_shadowit'] = df_shadowit['ind_criterio_blaklist'] + df_shadowit['ind_criterio_aval'] + df_shadowit['ind_criterio_categoria_shadowit'] + df_shadowit['ind_criterio_categoria_shadowit_jarvix'] + df_shadowit['ind_criterio_whithlist'] + df_shadowit['ind_criterio_cloud_confidence_high']
        df_shadowit['ind_criterio_shadowit'] = np.where(df_shadowit['vl_criterio_shadowit']>=7,1, 0)

        
        df_shadowit['dt_execucao_sgs'] = datetime.datetime.now()
        df_shadowit = df_shadowit.fillna("-")
        

        logger.info('Gravando na collection shadowit_apiexterna') 
        df_shadowit_resumo = df_shadowit[(df_shadowit['ind_criterio_shadowit']==1)]
        df_shadowit_resumo = df_shadowit_resumo[['tp_shadowit_tb','dt_evento','nm_aplicacao','nm_url_completo','qt_acesso_realizados',
                                        'id_usuario','nm_usuario', 'id_usario_hierarquia','nm_gestao_n1','nm_gestao_n2','nm_gestao_n3','nm_area',
                                        'tp_classificacao_cci',
                                        'ind_criterio_blaklist','ind_criterio_aval','ind_criterio_categoria_shadowit','ind_criterio_categoria_shadowit_jarvix','ind_criterio_whithlist','ind_criterio_cloud_confidence_high',
                                        'is_shadowit','jarvix_comment','fl_match_nestskope_apps',
                                        'vl_criterio_shadowit','ind_criterio_shadowit',
                                        'nm_categoria_aplicacao','nm_grupo_regra_risco','dt_execucao_sgs']]

        mongo_insert_collection('shadowit_apiexterna',df_shadowit_resumo)
    
        nr_linhas = df_shadowit_resumo.shape[0]
        job["total"] = nr_linhas
        logger.info('Fim')
    except Exception as inst:
        job['details']['erro'] = inst
        job["end"] = datetime.datetime.now()
        logger.info("Job {} finalizado Total: {} Erros: {}".format(job_objectid, job["total"], job["error"]))
        mongo_sgs.jobs.update_one({"_id": job_objectid}, {"$set": job}) 

    job["end"] = datetime.datetime.now()
    logger.info("Job {} finalizado Total: {} Erros: {}".format(job_objectid, job["total"], job["error"]))
    mongo_sgs.jobs.update_one({"_id": job_objectid}, {"$set": job})         


#######################################################################################################

@bp.cli.command('api_interna') 
def api_interna():

    # pd.set_option("display.max_rows", None)  # Exibir todas as linhas
    # pd.set_option("display.max_columns", None)  # Exibir todas as colunas
    # pd.set_option("display.width", 1000)  # Ajustar a largura para evitar quebra de linha
    # pd.set_option("display.colheader_justify", "left")  # Ajustar cabeçalhos à esquerda
    # pd.set_option("display.max_colwidth", None) # Exibir colunas longas sem trunca
    # logger.info(f"Shadow IT SaaS: Iniciando Processamento")

    search_query = f'''index=xp_crowdstrike_fdr event_simpleName="NetworkConnectIP*" 
            | eval is_local_ip=if( cidrmatch("10.0.0.0/8", RemoteAddressIP4) OR 
                                   cidrmatch("172.16.0.0/12", RemoteAddressIP4) OR 
                                   cidrmatch("192.168.0.0/16", RemoteAddressIP4) OR 
                                   cidrmatch("FE80::/10", RemoteAddressIP4) OR 
                                   cidrmatch("FC00::/7", RemoteAddressIP4), "true", "false" ) 
            | lookup xp_crowdstrike_ids.csv aid OUTPUT username, workstation, Nome 
            | eval user=coalesce(username,"N/A") 
            | lookup xp_ips_conhecidos_shadow.csv RemoteAddressIP4 OUTPUT validoIP 
            | search NOT (validoIP="true") 
            | lookup xp_processos_conhecidos_shadow.csv ContextBaseFileName OUTPUT validoProcesso 
            | search NOT (validoProcesso="true") 
            | eval time=strftime(_time,"%Y-%m-%dT%H:%M") 
            | where isnotnull(workstation) 
            | where is_local_ip="true" 
            | search NOT(RemotePort=0 OR 
                         RemotePort=389 OR 
                         RemotePort=53 OR 
                         RemotePort=67 OR 
                         RemotePort=137 OR 
                         RemotePort=135 OR 
                         RemotePort=7680) 
            | eval range_conhecido=if(cidrmatch("10.101.56.0/22",RemoteAddressIP4),"true", "false") 
            | where range_conhecido="false" 
            | search NOT ( RemoteAddressIP4="10.100.104.4" OR RemoteAddressIP4="10.100.104.5" OR 
                           RemoteAddressIP4="10.16.15.100" OR RemoteAddressIP4="10.16.15.101" OR 
                           RemoteAddressIP4="10.100.36.5" OR RemoteAddressIP4="10.117.64.6" OR 
                           RemoteAddressIP4="10.117.64.7" OR RemoteAddressIP4="10.100.36.6" OR 
                           RemoteAddressIP4="10.88.9.110" OR RemoteAddressIP4="10.100.4.5" OR 
                           RemoteAddressIP4="10.100.4.6" OR RemoteAddressIP4="10.116.64.7" OR 
                           RemoteAddressIP4="10.116.64.6" OR RemoteAddressIP4="10.130.132.100" OR 
                           RemoteAddressIP4="10.130.133.101" OR RemoteAddressIP4="10.130.164.100" OR 
                           RemoteAddressIP4="10.130.165.101" OR RemoteAddressIP4="10.78.47.10" OR 
                           RemoteAddressIP4="10.78.47.11" OR RemoteAddressIP4="10.14.20.100" OR 
                           RemoteAddressIP4="10.14.20.101" OR RemoteAddressIP4="10.29.128.100" OR 
                           RemoteAddressIP4="10.29.128.101" OR RemoteAddressIP4="10.75.47.10" OR 
                           RemoteAddressIP4="10.75.47.11" OR RemoteAddressIP4="10.48.7.101" OR 
                           RemoteAddressIP4="10.48.7.102" OR RemoteAddressIP4="10.48.7.4" OR 
                           RemoteAddressIP4="10.55.30.101" OR RemoteAddressIP4="10.55.30.102" OR 
                           RemoteAddressIP4="10.55.30.10" OR RemoteAddressIP4="10.0.0.1" ) 
            | head 100
            | stats values(ContextBaseFileName) as nm_arquivo_completo
             ,values(time) as dt_evento
             ,values(user) as id_account
             by RemoteAddressIP4
             ,RemotePort
       '''
    result = search(search_query,'-3h') # passar via paramentro do view no SPL campo recorrencia
    logger.info(result)

    '''
    logger.info('------- View ------------')
    view = mongo_sgs.shadowit_regras.find_one({'title':'shadowit_apinterna'})
    view_spl = view['spl']
    view_earliest_time = view['earliest_time']
    '''

    # OK
    logger.info('------- Results ------------')
    df_spl = pd.DataFrame(result['results'])
    df_spl['nm_arquivo_lower'] = df_spl['nm_arquivo_completo'].str.replace('.exe', '')
    df_spl['nm_arquivo_upper'] = df_spl['nm_arquivo_lower'].str.replace('.EXE', '')
    df_spl = df_spl[['nm_arquivo_completo','nm_arquivo_upper','dt_evento','id_account','RemoteAddressIP4','RemotePort']].rename(columns={'nm_arquivo_upper':'nm_arquivo','RemoteAddressIP4':'nu_ip','RemotePort':'nu_porta_remota'})
    logger.info('Print Dataframe') 
    logger.info(df_spl)
    
    
    # Hierarquia
    logger.info('------------ Hierarquia ------------')
    df_hierarquia = search_hierarquia_usuario(df_spl, 'id')
    df_hierarquia = search_hierarquia_usuario(df_hierarquia, 'mail')
    df_hierarquia = df_hierarquia [['nome','mail','n1','n2','n3','squad']].rename(columns={'nome':'nm_usuario','mail':'id_usario_hierarquia','n1':'nm_gestao_n1','n2':'nm_gestao_n2','n3':'nm_gestao_n3','squad':'nm_area'})
    logger.info(df_hierarquia.head(5))

    logger.info(type(df_hierarquia))
    
    # Merge
    logger.info('Merge')
    df_shadowit_hierarquia = pd.merge(df_spl, df_hierarquia, left_on = 'id_account', right_on = 'id_usario_hierarquia', how = 'left')
 
    # Criterios
    # OK
    
    logger.info('flag para Criterios')
    df_shadowit_criterios = df_shadowit_hierarquia
    df_shadowit_criterios['tp_shadowit_tb'] = 'api_interna'

    df_shadowit_criterios['nu_ip_limpo'] = df_shadowit_criterios['nu_ip'].str.replace('.','')
    # Caso o retorno der 1 então positivo para IP caso der 0 positivo para Swagger
    df_shadowit_criterios['fl_swagger_firewall'] = np.where(df_shadowit_criterios['nu_ip'].str.isnumeric(),1,0)

    df_shadowit_criterios['fl_cadastro_swagger'] = np.where(df_shadowit_criterios['fl_swagger_firewall']==0,1,0)
    df_shadowit_criterios['fl_cadastrado_firewall'] = np.where(df_shadowit_criterios['fl_swagger_firewall']==1,1,0)
    df_shadowit_criterios['fl_cadastrado_porta'] = np.where((df_shadowit_criterios['nu_porta_remota']=='443') | (df_shadowit_criterios['nu_porta_remota']=='80'),1,0)
    
    
    # OK
    logger.info('Criando os critérios Shadowit Api interna') 
    df_criterios_shadowit = search_criterio_shadowit()
    df_criterios_shadowit_1 = df_criterios_shadowit[df_criterios_shadowit['id']==1]
    df_criterios_shadowit_2 = df_criterios_shadowit[df_criterios_shadowit['id']==2]
    df_criterios_shadowit_3 = df_criterios_shadowit[df_criterios_shadowit['id']==3]

    # OK
    logger.info('Aplicando critérios Shadowit 1: ind_cadastro_swagger')
    df_shadowit = pd.merge(df_shadowit_criterios, df_criterios_shadowit_1, left_on = 'tp_shadowit_tb' , right_on = 'tp_shadowit', how = 'left')
    df_shadowit['ind_cadastro_swagger'] = np.where(df_shadowit['fl_cadastro_swagger']==0, df_criterios_shadowit_1['Peso'], 0)
    df_shadowit = df_shadowit.drop(columns = ['_id_x','_id_y','tp_shadowit','id','Indicador','Peso'])

    # OK
    logger.info('Aplicando critérios Shadowit 2: ind_cadastrado_firewall') 
    df_shadowit = pd.merge(df_shadowit_criterios, df_criterios_shadowit_2, left_on = 'tp_shadowit_tb' , right_on = 'tp_shadowit', how = 'left')
    df_shadowit['ind_cadastrado_firewall'] = np.where(df_shadowit['fl_cadastrado_firewall']==0, df_criterios_shadowit_2['Peso'], 0)
    df_shadowit = df_shadowit.drop(columns = ['_id_x','_id_y','tp_shadowit','id','Indicador','Peso'])

    # FALTA DEFINIR UM CRITERIO
    logger.info('Aplicando critérios Shadowit 3: ind_porta')
    df_shadowit = pd.merge(df_shadowit_criterios, df_criterios_shadowit_3, left_on = 'tp_shadowit_tb' , right_on = 'tp_shadowit', how = 'left')
    df_shadowit['ind_porta'] = np.where(df_shadowit['']==0, df_criterios_shadowit_3['Peso'], 0)
    df_shadowit = df_shadowit.drop(columns = ['_id_x','_id_y','tp_shadowit','id','Indicador','Peso'])

    # OK
    logger.info('Aplicando critério Shadowit final') 
    df_shadowit['vl_criterio_shadowit'] = df_shadowit['ind_cadastro_swagger'] + df_shadowit['ind_cadastrado_firewall'] + df_shadowit['ind_porta']

    # VERIFICAR SE O CRITERIO ESTA CORRETO
    df_shadowit['ind_criterio_shadowit'] = np.where(df_shadowit['vl_criterio_shadowit']>=7,1, 0)

    # OK
    df_shadowit['dt_ingestão'] = datetime.datetime.now()

    # OK
    logger.info('Gravando na collection shadowit_apinterna') 
    df_shadowit_resumo = df_shadowit[(df_shadowit['ind_criterio_shadowit']==1)].fillna("-")
    df_shadowit_resumo = df_shadowit_resumo[['tp_shadowit_tb','dt_evento','id_usuario','nm_usuario','id_usario_hierarquia','nm_gestao_n1','nm_gestao_n2',
                                             'nm_gestao_n3','nm_area','nm_arquivo','nu_ip','nu_porta_remota','fl_cadastro_swagger','fl_cadastrado_firewall',
                                             'ind_criterio_shadowit','ind_cadastro_swagger','ind_cadastrado_firewall','ind_porta','dt_ingestão']]
    
    # OK
    mongo_insert_collection('shadowit_apinterna',df_shadowit_resumo)

    # OK
    logger.info('Gravando na collection shadowit_apinterna_homologacao para homologacao')
    df_shadowit1 = df_shadowit[(df_shadowit['ind_criterio_shadowit']==1)].fillna("-")
    mongo_insert_collection('shadowit_apinterna_homologacao',df_shadowit1)

    # OK
    logger.info('Gravando na collection shadowit_apinterna_homologacao_0 para contra prova') 
    df_shadowit0 = df_shadowit[df_shadowit['ind_criterio_shadowit']==0].fillna("-")
    mongo_insert_collection('shadowit_apinterna_homologacao_0',df_shadowit0)
    '''
    # mongo_recriar_collection('shadowit_teste_apinterna',df_spl)
    mongo_recriar_collection('shadowit_teste_apinterna_hierarquia',df_shadowit_hierarquia)
     
    logger.info('fim')
    
app.register_blueprint(bp)