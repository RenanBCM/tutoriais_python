@bp.cli.command('scripts_dll_exe') 
def scripts_dll_exe():
    job_objectid, job = create_job("shadowit_dll", None, None, None)
    job={}
    job['details'] ={}
    job['details']['success'] =[]   
    job['details']['Fail'] =[]   
    job["total"]=0
    job["inserted"]=0
    job["error"]=0      
    
    try:
        # QUERY DLL
        logger.info('Lendo SPL da view shadowit_regras shadowit_dll') 
        view = mongo_sgs.shadowit_regras.find_one({'title':'shadowit_dll'})
        view_spl = view['spl']
        view_earliest_time = view['earliest_time']
        messagem = f'Executando script : {view_spl}. Earliest_time: {view_earliest_time}'
        job['details']['success'].append(messagem)
        # result = None

        try:
            # RESULT DLL
            result = search(view_spl,view_earliest_time)
            messagem = f'Consulta SPL executada'
            job['details']['success'].append(messagem)
            logger.info('Transformando resultado em DataFrame Pandas') 
            df_spl_shadowit_dll = pd.DataFrame(result['results'])
            messagem = f'A quantidade de registros retornando da consulta SPL foi : {df_spl_shadowit_dll.shape[0]}'
            logger.info(messagem)
            job['details']['success'].append(messagem)   

        except Exception as inst:
            logger.info (f'A consulta SPL FALHOU: {str(inst)}') 
            messagem = f'A consulta SPL FALHOU: {str(inst)}' 
            job['details']['Fail'] = messagem

        logger.info('Lendo SPL da view shadowit_regras shadowit_exe ') 
        view = mongo_sgs.shadowit_regras.find_one({'title':'shadowit_exe'})
        view_spl= view['spl']
        view_earliest_time = view['earliest_time']
        messagem = f'Executando script : {view_spl}. Earliest_time: {view_earliest_time}'
        job['details']['success'].append(messagem)
        # result = None

        try:
            result = search(view_spl,view_earliest_time)
            messagem = f'Consulta SPL executada'
            job['details']['success'].append(messagem)
            logger.info('Transformando resultado em DataFrame Pandas') 
            df_spl_shadowit_exe = pd.DataFrame(result['results'])
            messagem = f'A quantidade de registros retornando da consulta df_spl_shadowit_exe foi : {df_spl_shadowit_exe.shape[0]}'
            logger.info(messagem)
            job['details']['success'].append(messagem)   

        except Exception as inst:
            logger.info (f'A consulta SPL FALHOU: {str(inst)}') 
            messagem = f'A consulta SPL FALHOU: {str(inst)}' 
            job['details']['Fail'] = messagem
        
        
        if df_spl_shadowit_dll.shape[0] != 0 and df_spl_shadowit_exe.shape[0] != 0:
            df_spl_shadowit_dll['tp_shadowit_tb'] = 'dll'
            df_spl_shadowit_exe['tp_shadowit_tb'] = 'exe'

            df_spl = pd.concat([df_spl_shadowit_dll, df_spl_shadowit_exe],ignore_index=True)
            messagem = f'Dataframes de df_spl_shadowit_dll e df_spl_shadowit_exe foram unificados'
            logger.info(messagem)
            job['details']['success'].append(messagem)  

        elif df_spl_shadowit_dll.shape[0] != 0 and df_spl_shadowit_exe.shape[0] ==0 :
            df_spl_shadowit_dll['tp_shadowit_tb'] = 'dll'
            df_spl = df_spl_shadowit_dll
            messagem = f'Dataframes de df_spl_shadowit_dll é o unico Dataframe'
            logger.info(messagem)
            job['details']['success'].append(messagem)  


        elif df_spl_shadowit_dll.shape[0] == 0 and df_spl_shadowit_exe.shape[0] != 0 :
            df_spl_shadowit_exe['tp_shadowit_tb'] = 'exe'
            df_spl = df_spl_shadowit_exe
            messagem = f'Dataframes de df_spl_shadowit_exe é o unico Dataframe'
            logger.info(messagem)
            job['details']['success'].append(messagem) 
        

        if df_spl.shape[0] == 0:
            messagem = f'Processeo Encerrado'
            job['details']['success'].append(messagem) 
            job["total"] = df_spl.shape[0]

        else:
            logger.info(df_spl.dtypes  )
            df_spl['id_account_upper'] = df_spl['id_account'].str.upper()
            logger.info('selecionando dados Dataframe')
            df_spl = df_spl[['id_account_upper','dt_evento', 'nm_arquivo_original', 'nm_compania', 'workstation','tp_shadowit_tb']].rename(columns={'nm_compania':'nm_aplicacao', 'id_account_upper':'id_account', 'workstation':'id_estacao_trabalho'})
            df_spl["nm_arquivo"] = df_spl["nm_arquivo_original"].apply(lambda x: ", ".join([i for i in x if i]) if isinstance(x, list) else str(x))
            messagem = f'A quantide de registros retornando da consulta SPL foi : {df_spl.shape[0]}'
            job['details']['success'].append(messagem)   
            # logger.info(df_spl)
        
            # >>>>>>>>>> AVAL <<<<<<<<<<<<
            logger.info('Procurando avaliacoes')
            df_aval = search_aval(df_spl)
            # logger.info(df_aval)
            messagem = f'Criado DataFrame de avaliacoes'
            job['details']['success'].append(messagem)
        
            # >>>>>>>>>> HIERARQUIA <<<<<<<<<<<<
            logger.info('Procurando hierarquia')
            df_hierarquia = search_hierarquia_usuario(df_spl,'id_api_interna')
            df_hierarquia = search_hierarquia_usuario(df_hierarquia,'mail_api_interna')
            df_hierarquia = df_hierarquia[['nome','mail','n1','n2','n3','n4','n5','squad','id_ldap']].rename(columns={'nome':'nm_usuario','n1':'nm_gestao_n1','n2':'nm_gestao_n2','n3':'nm_gestao_n3','n4':'nm_gestao_n4','n5':'nm_gestao_n5','squad':'nm_area'}) 
            messagem = f'Criado DataFrames de hierarquia'
            job['details']['success'].append(messagem)
        
            logger.info('Realizando joins')   
            df_shadowit_hierarquia = pd.merge(df_spl, df_hierarquia, left_on = 'id_account', right_on = 'id_ldap', how = 'left')
            df_shadowit_aval = pd.merge(df_shadowit_hierarquia, df_aval, left_on = 'nm_aplicacao' , right_on = 'nameService', how = 'left')
            messagem = f'Joins entre a consulta do spl, hierarquia e avaliacoes realizados'
            job['details']['success'].append(messagem)    
        
            logger.info('criando campos de flag para Criterios')
            df_shadowit_criterios = df_shadowit_aval
            # df_shadowit_criterios['tp_shadowit_tb'] = 'dll'
            df_shadowit_criterios['fl_aval'] = np.where((df_shadowit_criterios['nr_avaliacao'].isna()) | (df_shadowit_criterios['nr_avaliacao']== '-') ,1,0)
            df_shadowit_criterios['fl_workstation'] = np.where((df_shadowit_criterios['id_estacao_trabalho'].isnull()) ,0,1) 
            df_shadowit_criterios['fl_is_shadowit'] = np.where(df_shadowit_criterios['is_shadowit']== 'Sim',1, 0)
            df_shadowit_criterios['fl_match_nestskope_apps'] = np.where((df_shadowit_criterios['is_shadowit']== 'Sim') | (df_shadowit_criterios['is_shadowit']== 'Não'),1, 0)

            logger.info('Criando os critérios Shadowit') 
            df_criterios_shadowit = search_criterio_shadowit('dll')
            df_criterios_shadowit_1 = df_criterios_shadowit[df_criterios_shadowit['id']==1][['_id','tp_shadowit','id','Peso','Indicador']].astype({'Peso': 'float'})
            df_criterios_shadowit_2 = df_criterios_shadowit[df_criterios_shadowit['id']==2][['_id','tp_shadowit','id','Peso','Indicador']].astype({'Peso': 'float'})
        
            # ind_criterio_workstation - Peso 3
            logger.info('aplicando critérios Shadowit 1: ind_criterio_workstation') 
            df_shadowit = pd.merge(df_shadowit_criterios, df_criterios_shadowit_1, left_on = 'tp_shadowit_tb' , right_on = 'tp_shadowit', how = 'left')
            df_shadowit['ind_criterio_workstation'] = np.where(df_shadowit['fl_workstation']==1, df_criterios_shadowit_1['Peso'], 0)
            df_shadowit = df_shadowit.drop(columns = ['_id','tp_shadowit','id','Indicador','Peso'])
        
            # ind_criterio_aval - Peso 4
            logger.info('Aplicando critérios Shadowit 2: ind_criterio_aval') 
            df_shadowit = pd.merge(df_shadowit, df_criterios_shadowit_2, left_on = 'tp_shadowit_tb' , right_on = 'tp_shadowit', how = 'left')
            df_shadowit['ind_criterio_aval'] = np.where(df_shadowit['fl_aval']==1, df_criterios_shadowit_2['Peso'], 0)
            df_shadowit = df_shadowit.drop(columns = ['_id','tp_shadowit','id','Indicador','Peso'])
        
            logger.info('Aplicando critério Shadowit final') 
            df_shadowit['vl_criterio_shadowit'] = df_shadowit['ind_criterio_workstation'] + df_shadowit['ind_criterio_aval'] 
            df_shadowit['ind_criterio_shadowit'] = np.where(df_shadowit['vl_criterio_shadowit']>=7,1, 0)
            messagem = f'Criado critérios Shadowit'
            job['details']['success'].append(messagem)
        
            df_shadowit['dt_execucao_sgs'] = datetime.datetime.now()
            df_shadowit["job_id"] = str(job_objectid)
            df_shadowit = df_shadowit.fillna("-")

            logger.info('Gravando na collection shadowit_dll_exe') 
            df_shadowit_resumo = df_shadowit[(df_shadowit['ind_criterio_shadowit']==1)]
            df_shadowit_resumo = df_shadowit_resumo[['tp_shadowit_tb','dt_evento','nm_aplicacao','nm_arquivo',
                                            'id_account','id_estacao_trabalho','nm_usuario', 'mail','nm_gestao_n1','nm_gestao_n2','nm_gestao_n3','nm_gestao_n4','nm_gestao_n5','nm_area',
                                            'is_shadowit','jarvix_comment',
                                            'fl_aval','fl_workstation','fl_is_shadowit','fl_match_nestskope_apps',
                                            'ind_criterio_workstation','ind_criterio_aval',
                                            'vl_criterio_shadowit','ind_criterio_shadowit','dt_execucao_sgs']]
        
            nr_linhas = df_shadowit_resumo.shape[0] 
            messagem = f'A quantide de registros shadowit após a aplicaçaõ de critérios são: {nr_linhas}'
            job['details']['success'].append(messagem)
            
            try:
                logger.info(f'Salvando os dados na collection shadowit_saas pela função insert many' )
                messagem = f'Salvando os dados na collection shadowit_saas pela função insert many: {nr_linhas}. AGUARDANDO A CONFIRMACAO DA GRAVACAO...'
                resultado_insert, total_documentos_escritos, total_doc_nao_gravados, qtd_doc_erro_maior_16m, qtd_doc_erro = mongo_insert_many_resiliente('shadowit_scripts_dll_exe', df_shadowit_resumo,job)
                job["inserted"] = total_documentos_escritos
                job["error"]= total_doc_nao_gravados
                job["total"] = nr_linhas
                job['details']['success'].append(resultado_insert)  
                logger.info('Fim')
            except Exception as inst:
                job["total"] = 0
                job['details']['Fail'] = str(inst)
                logger.info(f'Nao foi possivel salvar os dados na collection pela função imongo_insert_many_resiliente: {inst}' )
        
    except Exception as inst:
        job["end"] = datetime.datetime.now()
        job["total"] = 0
        job['details']['error'] =  f'Job {job_objectid} finalizado com ERRO: {str(inst)}; {messagem}'
        logger.error("Job {} finalizado com ERRO: {}".format(job_objectid, job['details']['error']))
        mongo_sgs.jobs.update_one({"_id": job_objectid}, {"$set": job}) 
        
    job["end"] = datetime.datetime.now()
    logger.info("Job {} finalizado Total: {} success: {}".format(job_objectid, job["total"],job["inserted"],job["error"],job["details"].get('success','Sem log de sucesso')))
    mongo_sgs.jobs.update_one({"_id": job_objectid}, {"$set": job})