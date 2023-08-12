import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import missingno as msno
import altair as alt
import time


@st.cache_data
def converte_csv(df):
    return df.to_csv(index = False).encode('utf-8')



def mensagem_sucesso():
    sucesso = st.success('Arquivo baixado com sucesso', icon = "✅") 
    time.sleep(6)
    sucesso.empty()
    

st.title('DADOS BRUTOS')



#Leitura dos dados
dados = pd.read_csv('23CIDS.csv', sep=',', dtype=str)
dados = dados.dropna(axis=1)
dados['ANO_CMPT'] = dados['ANO_CMPT'].astype('int64')
dados['MORTE'] = dados['MORTE'].astype('int64')
dados['DIAS_PERM'] = dados['DIAS_PERM'].astype('int64')
dados['IDADE'] = dados['IDADE'].astype('int64')



with st.expander('Colunas'):
    colunas = st.multiselect('Selecione as colunas', list(dados.columns), list(dados.columns))
    
    
st.sidebar.title('Filtros')
with st.sidebar.expander('ANO_CMPT'):
    ANO_CMPT = st.slider('Selecione o ano', 2008, 2021, (2008,2021))
    
with st.sidebar.expander('IDADE'):
    IDADE = st.slider('Selecione a idade', 0, 120, (0,120))
    
with st.sidebar.expander('res_CODIGO_UF'):
    res_CODIGO_UF = st.multiselect('Selecione o codigo do estado', dados['res_CODIGO_UF'].unique(), dados['res_CODIGO_UF'].unique())    
    
with st.sidebar.expander('DIAS_PERM'):
   DIAS_PERM =  st.slider('Dias de permanencia', 0, 365, (0,365))
    
with st.sidebar.expander('DIAG_PRINC'):
   DIAG_PRINC = st.multiselect('Selecione O CID', dados['DIAG_PRINC'].unique(), dados['DIAG_PRINC'].unique())
   
   
   
query = '''
@ANO_CMPT[0] <= ANO_CMPT <= @ANO_CMPT[1] and \
@IDADE[0] <= IDADE <= @IDADE[1] and \
res_CODIGO_UF in @res_CODIGO_UF and \
@DIAS_PERM[0]<= `DIAS_PERM` <= @DIAS_PERM[1] and \
`DIAG_PRINC` in @ DIAG_PRINC
'''
   
   
dados_filtrados = dados.query(query)
dados_filtrados = dados_filtrados[colunas]



st.dataframe(dados_filtrados)

st.markdown(f'A tabela possui :blue[{dados_filtrados.shape[0]}] linhas e :blue[{dados_filtrados.shape[1]}] colunas')


def preparando():
    msg = st.toast('Preparando...')
    time.sleep(1)
    msg.toast('Organizando tabela...')
    time.sleep(1)
    msg.toast('Pronto!', icon = "🤖")



st.markdown('Escreva um nome para o arquivo')
coluna1 , coluna2 = st.columns(2)
with coluna1:
    nome_arquivo = st.text_input('', label_visibility='collapsed', value='dados')
    nome_arquivo += '.csv'
    
with coluna2:
    st.download_button('Fazer o download da tabela em csv', data= converte_csv(dados_filtrados), file_name= nome_arquivo, mime= 'text/csv', on_click= mensagem_sucesso)
    if converte_csv(dados_filtrados):
        preparando()
    

   