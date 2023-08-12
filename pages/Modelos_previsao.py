import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import missingno as msno
import altair as alt
from PIL import Image

#config da pagina
st.set_page_config(layout= 'wide',page_icon=':computer:')

def formata_numero(valor, prefixo = ''):
    for unidade in ['', 'mil']:
        if valor <1000:
            return f'{prefixo} {valor:.2f} {unidade}'
        valor /= 1000
    return f'{prefixo} {valor:.2f} milhoes'

contador = 0

with st.container():
    #H1
    st.divider()
    st.title(':desktop_computer: MACHINE LEARNING (SIH) HEMORRAGIA DIGESTIVA :skull::drop_of_blood:') 
    st.divider()
    
    
#Leitura dos dados

dadosMachine = pd.read_csv('dfFinal.csv', sep=';')

#col1.metric("**Óbitos em todo Periodo**", "37.328")

st.title('Modelos de Previsão')
st.divider()
col1,col2,col3 = st.columns(3)
with col1:
        st.header('Arvore de decisão de Classificação')
        image = Image.open('./arvoreclass.png')
        st.image(image, caption='Arvore de decisão de Classificação')
with st.container():
        col1.metric('**Accuracy médio 88.48%**', 'Intervalo [87.92, 89.04]','10,92%')
        
        
with col2:
    with st.container():
        st.header('Arvore de decisão de Regressão')
        image = Image.open('./arvoreRegr.png')
        st.image(image, caption='Arvore de decisão de Regressão ')
        st.header('MAE: 0.40')
        col2.metric('MAE: 0.4011725904574862','RMSE: 0.4472551507153818','-12%')
        st.header('MSE: 0.20003716984143888')
with col3:
    with st.container():
        st.header('Random Forest')
        image1 = Image.open('./Comeco.png')
        image2 = Image.open('./meio.png')
        image3 = Image.open('./fim.png')
        st.image(image1, caption='')
        st.image(image2, caption='')
        st.image(image3, caption='')
        st.write('3 primeiras arvores')
        
        
        
        
st.divider()

st.dataframe(dadosMachine, hide_index=True)
    
st.divider()
st.markdown('Desenvolvido por **ALAN MOLTER** :technologist:')
st.divider()

contador = 1

if contador == 1:
        st.stop()