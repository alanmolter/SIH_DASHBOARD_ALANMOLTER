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

contador = 0

#config da pagina
st.set_page_config(layout= 'wide',page_icon=':computer:')

def formata_numero(valor, prefixo = ''):
    for unidade in ['', 'mil']:
        if valor <1000:
            return f'{prefixo} {valor:.2f} {unidade}'
        valor /= 1000
    return f'{prefixo} {valor:.2f} milhoes'


with st.container():
    
    st.divider()
    st.title(':desktop_computer: MACHINE LEARNING (SIH) HEMORRAGIA DIGESTIVA :skull::drop_of_blood:') 
    st.divider()
    st.write('A análise exploratória pode demorar alguns minutos, por favor **espere um pouco** a pagina ser carregada.')
    
    
#Leitura dos dados
dados = pd.read_csv('23CIDS.csv', sep=',', dtype=str)
dados = dados.dropna(axis=1)
dados['ANO_CMPT'] = dados['ANO_CMPT'].astype('int64')
dados['MORTE'] = dados['MORTE'].astype('int64')
dados['DIAS_PERM'] = dados['DIAS_PERM'].astype('int64')
dados['IDADE'] = dados['IDADE'].astype('int64')



df3 =pd.DataFrame(dados['IDADE'])
df3['Dias_de_permanencia'] = dados['DIAS_PERM']

df4 = pd.DataFrame(dados['MORTE']==1)
df4['Dias'] = dados['DIAS_PERM'].astype('int64')


chart = alt.Chart(dados).mark_boxplot(extent='min-max').encode(
    x='DIAG_PRINC',
    y='IDADE'
)



#fig6 = alt.Chart(df3).mark_circle().encode(
#    x='Dias_de_permanencia',
#    y='IDADE',
 #   ).interactive()



fig7 = alt.Chart(df4).mark_circle().encode(
    x='MORTE',
    y='Dias',
    ).interactive()



fig8, ax = plt.subplots()
ax.hist(dados['IDADE'],label= 'Idades',bins=30)



st.title('Analise Exploratória')
col1,col2 = st.columns(2)
with col1:
        st.write(dados)
        st.title('Distribuição da faixa etária')
        st.pyplot(fig8,use_container_width=True)
        
        

with col2:
        #st.altair_chart(fig6, theme="streamlit", use_container_width=True)
        st.altair_chart(fig7, theme="streamlit", use_container_width=True)
        st.divider()
        st.altair_chart(chart, theme="streamlit", use_container_width=True)
        
        
    
    
col1, col2, col3 = st.columns(3)
col1.metric("**Óbitos em todo Periodo**", "37.328")
col2.metric("**Óbitos 2020**", "3.134", "34.194")
col3.metric("**Óbitos 2021**", "1.881", "-1.253")



st.divider()
st.markdown('Desenvolvido por **ALAN MOLTER** :technologist:')
st.divider()


if contador == 1:
        st.stop()