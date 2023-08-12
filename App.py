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
    #H1
    st.divider()
    st.title(':desktop_computer: MACHINE LEARNING (SIH) HEMORRAGIA DIGESTIVA :skull::drop_of_blood:') 
    st.divider()
    

#Leitura dos dados
dados = pd.read_csv('23CIDS.csv', sep=',', dtype=str)
dados = dados.dropna(axis=1)
dados['ANO_CMPT'] = dados['ANO_CMPT'].astype('int64')
dados['MORTE'] = dados['MORTE'].astype('int64')
dados['DIAS_PERM'] = dados['DIAS_PERM'].astype('int64')
dados['IDADE'] = dados['IDADE'].astype('int64')





#Tabelas
mortes = pd.DataFrame(dados['MORTE'])
mortes['ANO_CMPT'] =dados['ANO_CMPT']


df1 = dados[dados.MORTE == 1].groupby(["ANO_CMPT"]).sum()

df2 = pd.DataFrame(df1['MORTE'])
df2['Aumento'] = df2.MORTE.shift(-1).div(df2.MORTE) - 1
df2['Aumento_Direto'] = df2.MORTE.pct_change()
df2['Aceleração'] = df2['Aumento'].diff()
df2['media_movel'] = df2['MORTE'].rolling(1).mean()


############################################################################################################################################

dfSul = dados[(dados.res_CODIGO_UF == '41') | (dados.res_CODIGO_UF == '42') | (dados.res_CODIGO_UF == '43') & (dados.MORTE == 1)]
dfSul2008 = dados[(dados.res_CODIGO_UF == '41') | (dados.res_CODIGO_UF == '42') | (dados.res_CODIGO_UF == '43') & (dados.MORTE == 1) & (dados.ANO_CMPT == 2008)]
dfSul2015 = dados[(dados.res_CODIGO_UF == '41') | (dados.res_CODIGO_UF == '42') | (dados.res_CODIGO_UF == '43') & (dados.MORTE == 1) & (dados.ANO_CMPT == 2015)]
dfSul2020 = dados[(dados.res_CODIGO_UF == '41') | (dados.res_CODIGO_UF == '42') | (dados.res_CODIGO_UF == '43') & (dados.MORTE == 1) & (dados.ANO_CMPT == 2020)]
dfSulmorte = dfSul.groupby(["ANO_CMPT"]).sum()
dfSul2 = dados[(dados.res_CODIGO_UF == '41')|(dados.res_CODIGO_UF == '42') | (dados.res_CODIGO_UF == '43')]

dfSulAceleracao = pd.DataFrame(dfSulmorte['MORTE'])
dfSulAceleracao['Aumento'] = dfSulAceleracao.MORTE.shift(-1).div(df2.MORTE) - 1
dfSulAceleracao['Aumento_Direto'] = dfSulAceleracao.MORTE.pct_change()
dfSulAceleracao['Aceleração'] = dfSulAceleracao['Aumento'].diff()
dfSulAceleracao['media_movel'] = dfSulAceleracao['MORTE'].rolling(1).mean()


#################################################################################################################################################


dfSudeste = dados[(dados.res_CODIGO_UF == '31') | (dados.res_CODIGO_UF == '32') | (dados.res_CODIGO_UF == '33') | (dados.res_CODIGO_UF == '35') & (dados.MORTE == 1)]
dfSudeste2008 = dados[(dados.res_CODIGO_UF == '31') | (dados.res_CODIGO_UF == '32') | (dados.res_CODIGO_UF == '33') | (dados.res_CODIGO_UF == '35') & (dados.MORTE == 1)& (dados.ANO_CMPT == 2008)]
dfSudeste2015 = dados[(dados.res_CODIGO_UF == '31') | (dados.res_CODIGO_UF == '32') | (dados.res_CODIGO_UF == '33') | (dados.res_CODIGO_UF == '35') & (dados.MORTE == 1)& (dados.ANO_CMPT == 2015)]
dfSudeste2020 = dados[(dados.res_CODIGO_UF == '31') | (dados.res_CODIGO_UF == '32') | (dados.res_CODIGO_UF == '33') | (dados.res_CODIGO_UF == '35') & (dados.MORTE == 1)& (dados.ANO_CMPT == 2020)]
dfSudestemorte = dfSudeste.groupby(["ANO_CMPT"]).sum()
dfSudeste2 = dados[(dados.res_CODIGO_UF == '31')|(dados.res_CODIGO_UF == '32') | (dados.res_CODIGO_UF == '33') | (dados.res_CODIGO_UF == '35')]

dfSudesteAceleracao = pd.DataFrame(dfSudestemorte['MORTE'])
dfSudesteAceleracao['Aumento'] = dfSudesteAceleracao.MORTE.shift(-1).div(df2.MORTE) - 1
dfSudesteAceleracao['Aumento_Direto'] = dfSudesteAceleracao.MORTE.pct_change()
dfSudesteAceleracao['Aceleração'] = dfSudesteAceleracao['Aumento'].diff()
dfSudesteAceleracao['media_movel'] = dfSudesteAceleracao['MORTE'].rolling(1).mean()


###################################################################################################################################################################################
dfCentroOeste = dados[(dados.res_CODIGO_UF == '50') | (dados.res_CODIGO_UF == '51') | (dados.res_CODIGO_UF == '52') & (dados.MORTE == 1)]
dfCentroOeste2008 = dados[(dados.res_CODIGO_UF == '50') | (dados.res_CODIGO_UF == '51') | (dados.res_CODIGO_UF == '52') & (dados.MORTE == 1)& (dados.ANO_CMPT == 2008)]
dfCentroOeste2015 =  dados[(dados.res_CODIGO_UF == '50') | (dados.res_CODIGO_UF == '51') | (dados.res_CODIGO_UF == '52') & (dados.MORTE == 1)& (dados.ANO_CMPT == 2015)]
dfCentroOeste2020 =  dados[(dados.res_CODIGO_UF == '50') | (dados.res_CODIGO_UF == '51') | (dados.res_CODIGO_UF == '52') & (dados.MORTE == 1)& (dados.ANO_CMPT == 2020)]
dfCentroOestemorte = dfCentroOeste.groupby(["ANO_CMPT"]).sum()
dfCentroOeste2 = dados[(dados.res_CODIGO_UF == '50')|(dados.res_CODIGO_UF == '51') | (dados.res_CODIGO_UF == '52')]

dfCentroOesteAceleracao = pd.DataFrame(dfCentroOestemorte['MORTE'])
dfCentroOesteAceleracao['Aumento'] = dfCentroOesteAceleracao.MORTE.shift(-1).div(df2.MORTE) - 1
dfCentroOesteAceleracao['Aumento_Direto'] = dfCentroOesteAceleracao.MORTE.pct_change()
dfCentroOesteAceleracao['Aceleração'] = dfCentroOesteAceleracao['Aumento'].diff()
dfCentroOesteAceleracao['media_movel'] = dfCentroOesteAceleracao['MORTE'].rolling(1).mean()


######################################################################################################################################################

dfNordeste = dados[(dados.res_CODIGO_UF == '27') | (dados.res_CODIGO_UF == '29') | (dados.res_CODIGO_UF == '23') | (dados.res_CODIGO_UF == '21') | (dados.res_CODIGO_UF == '25') | (dados.res_CODIGO_UF == '26') | (dados.res_CODIGO_UF == '22') | (dados.res_CODIGO_UF == '24') | (dados.res_CODIGO_UF == '28') & (dados.MORTE == 1)]
dfNordeste2008 = dados[(dados.res_CODIGO_UF == '27') | (dados.res_CODIGO_UF == '29') | (dados.res_CODIGO_UF == '23') | (dados.res_CODIGO_UF == '21') | (dados.res_CODIGO_UF == '25') | (dados.res_CODIGO_UF == '26') | (dados.res_CODIGO_UF == '22') | (dados.res_CODIGO_UF == '24') | (dados.res_CODIGO_UF == '28') & (dados.MORTE == 1)& (dados.ANO_CMPT == 2008)]
dfNordeste2015 = dados[(dados.res_CODIGO_UF == '27') | (dados.res_CODIGO_UF == '29') | (dados.res_CODIGO_UF == '23') | (dados.res_CODIGO_UF == '21') | (dados.res_CODIGO_UF == '25') | (dados.res_CODIGO_UF == '26') | (dados.res_CODIGO_UF == '22') | (dados.res_CODIGO_UF == '24') | (dados.res_CODIGO_UF == '28') & (dados.MORTE == 1)& (dados.ANO_CMPT == 2015)]
dfNordeste2020 = dados[(dados.res_CODIGO_UF == '27') | (dados.res_CODIGO_UF == '29') | (dados.res_CODIGO_UF == '23') | (dados.res_CODIGO_UF == '21') | (dados.res_CODIGO_UF == '25') | (dados.res_CODIGO_UF == '26') | (dados.res_CODIGO_UF == '22') | (dados.res_CODIGO_UF == '24') | (dados.res_CODIGO_UF == '28') & (dados.MORTE == 1)& (dados.ANO_CMPT == 2020)]
dfNordestemorte = dfNordeste.groupby(["ANO_CMPT"]).sum()
dfNordeste2 = dados[(dados.res_CODIGO_UF == '27') | (dados.res_CODIGO_UF == '29') | (dados.res_CODIGO_UF == '23') | (dados.res_CODIGO_UF == '21') | (dados.res_CODIGO_UF == '25') | (dados.res_CODIGO_UF == '26') | (dados.res_CODIGO_UF == '22') | (dados.res_CODIGO_UF == '24') | (dados.res_CODIGO_UF == '28')]


dfNordesteAceleracao = pd.DataFrame(dfNordestemorte['MORTE'])
dfNordesteAceleracao['Aumento'] = dfNordesteAceleracao.MORTE.shift(-1).div(df2.MORTE) - 1
dfNordesteAceleracao['Aumento_Direto'] = dfNordesteAceleracao.MORTE.pct_change()
dfNordesteAceleracao['Aceleração'] = dfNordesteAceleracao['Aumento'].diff()
dfNordesteAceleracao['media_movel'] = dfNordesteAceleracao['MORTE'].rolling(1).mean()


######################################################################################################################################################

dfNorte = dados[(dados.res_CODIGO_UF == '12') | (dados.res_CODIGO_UF == '16') | (dados.res_CODIGO_UF == '13') | (dados.res_CODIGO_UF == '15') | (dados.res_CODIGO_UF == '11') | (dados.res_CODIGO_UF == '14') | (dados.res_CODIGO_UF == '117') & (dados.MORTE == 1)]
dfNorte2008 = dados[(dados.res_CODIGO_UF == '12') | (dados.res_CODIGO_UF == '16') | (dados.res_CODIGO_UF == '13') | (dados.res_CODIGO_UF == '15') | (dados.res_CODIGO_UF == '11') | (dados.res_CODIGO_UF == '14') | (dados.res_CODIGO_UF == '117') & (dados.MORTE == 1)& (dados.ANO_CMPT == 2008)]
dfNorte2015 =  dados[(dados.res_CODIGO_UF == '12') | (dados.res_CODIGO_UF == '16') | (dados.res_CODIGO_UF == '13') | (dados.res_CODIGO_UF == '15') | (dados.res_CODIGO_UF == '11') | (dados.res_CODIGO_UF == '14') | (dados.res_CODIGO_UF == '117') & (dados.MORTE == 1)& (dados.ANO_CMPT == 2015)]
dfNorte2020 =  dados[(dados.res_CODIGO_UF == '12') | (dados.res_CODIGO_UF == '16') | (dados.res_CODIGO_UF == '13') | (dados.res_CODIGO_UF == '15') | (dados.res_CODIGO_UF == '11') | (dados.res_CODIGO_UF == '14') | (dados.res_CODIGO_UF == '117') & (dados.MORTE == 1)& (dados.ANO_CMPT == 2020)]
dfNortemorte = dfNorte.groupby(["ANO_CMPT"]).sum()
dfNorte2 = dados[(dados.res_CODIGO_UF == '12') | (dados.res_CODIGO_UF == '16') | (dados.res_CODIGO_UF == '13') | (dados.res_CODIGO_UF == '15') | (dados.res_CODIGO_UF == '11') | (dados.res_CODIGO_UF == '14') | (dados.res_CODIGO_UF == '117')]

dfNorteAceleracao = pd.DataFrame(dfNortemorte['MORTE'])
dfNorteAceleracao['Aumento'] = dfNorteAceleracao.MORTE.shift(-1).div(df2.MORTE) - 1
dfNorteAceleracao['Aumento_Direto'] = dfNorteAceleracao.MORTE.pct_change()
dfNorteAceleracao['Aceleração'] = dfNorteAceleracao['Aumento'].diff()
dfNorteAceleracao['media_movel'] = dfNorteAceleracao['MORTE'].rolling(1).mean()

#################################################################################################################################################

##############################################################################################################################################

#GRAFICOS

def countPlot():
        fig = plt.figure(figsize=(10, 4))
        sns.countplot(x = "ANO_CMPT", data = mortes)
        st.pyplot(fig)


figu = plt.figure(figsize=(7,5))
sns.countplot(x = "ANO_CMPT", data = mortes)


#fig2, ax = plt.subplots()
#ax.hist(dados['IDADE'], bins=50)

fig3 = plt.figure(figsize=(10,7))
sns.set_palette("Accent")
sns.set_style("darkgrid", {"grid.color": ".5", "grid.linestyle": ":"})
ax = sns.lineplot(x='ANO_CMPT',y=dados['MORTE'] == 1, err_style="bars", errorbar=("se", 2), data=dados)
ax.figure.set_size_inches(10,7)
ax.set_title('Série temporal de mortes confirmadas',fontsize=20, fontweight="bold")


fig4 = plt.figure(figsize=(10,7))
ax2 = sns.lineplot(x='ANO_CMPT',y=df2['Aceleração'] , data=df2)
ax2.set_title('Velocidade de aceleração das mortes',fontsize=18)
ax2.figure.set_size_inches(12,6)


fig5 = plt.figure(figsize=(10,7))
sns.set_palette("Accent")
sns.set_style("darkgrid", {"grid.color": ".5", "grid.linestyle": ":"})
ax = sns.lineplot(x='ANO_CMPT',y=df2['media_movel'], data=df2)
ax.figure.set_size_inches(12,6)
ax.set_title('Média movel',fontsize=18)


#############################################################################################################################################

   
#estados = ['Brasil',11,12,13,14,15,16,17,21,22,23,24,25,26,27,28,29,31,32,33,34,35,41,42,43,50,51,52,53]

regioes = ['Brasil','Sul','Sudeste','Centro-oeste','Nordeste','Norte']

st.sidebar.title('Filtros')
regioes = st.sidebar.selectbox('Regiões', regioes)


if regioes == 'Brasil':
        regioes = ""
                           
elif regioes == 'Sul':
    figu = plt.figure(figsize=(7,5))
    sns.countplot(x = "ANO_CMPT", data = dfSul)
    
    fig3 = plt.figure(figsize=(10,7))
    sns.set_palette("Accent")
    sns.set_style("darkgrid", {"grid.color": ".5", "grid.linestyle": ":"})
    ax = sns.lineplot(x='ANO_CMPT',y=dados['MORTE'] == 1, err_style="bars", errorbar=("se", 2), data=dfSul2)
    ax.figure.set_size_inches(10,7)
    ax.set_title('Série temporal de mortes confirmadas',fontsize=20, fontweight="bold")
    
    
    fig4 = plt.figure(figsize=(10,7))
    ax2 = sns.lineplot(x='ANO_CMPT',y=dfSulAceleracao['Aceleração'] , data=dfSulAceleracao)
    ax2.set_title('Velocidade de aceleração das mortes',fontsize=18)
    ax2.figure.set_size_inches(12,6)
    
    
    fig5 = plt.figure(figsize=(10,7))
    sns.set_palette("Accent")
    sns.set_style("darkgrid", {"grid.color": ".5", "grid.linestyle": ":"})
    ax = sns.lineplot(x='ANO_CMPT',y=dfSulAceleracao['media_movel'], data=dfSulAceleracao)
    ax.figure.set_size_inches(12,6)
    ax.set_title('Média movel',fontsize=18)
    

elif regioes == 'Sudeste':
    figu = plt.figure(figsize=(7,5))
    sns.countplot(x = "ANO_CMPT", data = dfSudeste)      


    fig3 = plt.figure(figsize=(10,7))
    sns.set_palette("Accent")
    sns.set_style("darkgrid", {"grid.color": ".5", "grid.linestyle": ":"})
    ax = sns.lineplot(x='ANO_CMPT',y=dados['MORTE'] == 1, err_style="bars", errorbar=("se", 2), data=dfSudeste2)
    ax.figure.set_size_inches(10,7)
    ax.set_title('Série temporal de mortes confirmadas',fontsize=20, fontweight="bold")

    fig4 = plt.figure(figsize=(10,7))
    ax2 = sns.lineplot(x='ANO_CMPT',y=dfSudesteAceleracao['Aceleração'] , data=dfSudesteAceleracao)
    ax2.set_title('Velocidade de aceleração das mortes',fontsize=18)
    ax2.figure.set_size_inches(12,6)

    fig5 = plt.figure(figsize=(10,7))
    sns.set_palette("Accent")
    sns.set_style("darkgrid", {"grid.color": ".5", "grid.linestyle": ":"})
    ax = sns.lineplot(x='ANO_CMPT',y=dfSudesteAceleracao['media_movel'], data=dfSudesteAceleracao)
    ax.figure.set_size_inches(12,6)
    ax.set_title('Média movel',fontsize=18)

  
elif regioes == 'Centro-oeste':
    figu = plt.figure(figsize=(7,5))
    sns.countplot(x = "ANO_CMPT", data = dfCentroOeste)      


    fig3 = plt.figure(figsize=(10,7))
    sns.set_palette("Accent")
    sns.set_style("darkgrid", {"grid.color": ".5", "grid.linestyle": ":"})
    ax = sns.lineplot(x='ANO_CMPT',y=dados['MORTE'] == 1, err_style="bars", errorbar=("se", 2), data=dfCentroOeste2)
    ax.figure.set_size_inches(10,7)
    ax.set_title('Série temporal de mortes confirmadas',fontsize=20, fontweight="bold")

    fig4 = plt.figure(figsize=(10,7))
    ax2 = sns.lineplot(x='ANO_CMPT',y=dfSudesteAceleracao['Aceleração'] , data=dfCentroOesteAceleracao)
    ax2.set_title('Velocidade de aceleração das mortes',fontsize=18)
    ax2.figure.set_size_inches(12,6)

    fig5 = plt.figure(figsize=(10,7))
    sns.set_palette("Accent")
    sns.set_style("darkgrid", {"grid.color": ".5", "grid.linestyle": ":"})
    ax = sns.lineplot(x='ANO_CMPT',y=dfSudesteAceleracao['media_movel'], data=dfCentroOesteAceleracao)
    ax.figure.set_size_inches(12,6)
    ax.set_title('Média movel',fontsize=18)  
  
  
  
  
  
elif regioes == 'Nordeste':
    figu = plt.figure(figsize=(7,5))
    sns.countplot(x = "ANO_CMPT", data= dfNordeste)      


    fig3 = plt.figure(figsize=(10,7))
    sns.set_palette("Accent")
    sns.set_style("darkgrid", {"grid.color": ".5", "grid.linestyle": ":"})
    ax = sns.lineplot(x='ANO_CMPT',y=dados['MORTE'] == 1, err_style="bars", errorbar=("se", 2), data=dfNordeste2)
    ax.figure.set_size_inches(10,7)
    ax.set_title('Série temporal de mortes confirmadas',fontsize=20, fontweight="bold")

    fig4 = plt.figure(figsize=(10,7))
    ax2 = sns.lineplot(x='ANO_CMPT',y=dfSudesteAceleracao['Aceleração'] , data=dfNordesteAceleracao)
    ax2.set_title('Velocidade de aceleração das mortes',fontsize=18)
    ax2.figure.set_size_inches(12,6)

    fig5 = plt.figure(figsize=(10,7))
    sns.set_palette("Accent")
    sns.set_style("darkgrid", {"grid.color": ".5", "grid.linestyle": ":"})
    ax = sns.lineplot(x='ANO_CMPT',y=dfSudesteAceleracao['media_movel'], data=dfNordesteAceleracao)
    ax.figure.set_size_inches(12,6)
    ax.set_title('Média movel',fontsize=18)
  
  
  
  
elif regioes == 'Norte':
    figu = plt.figure(figsize=(7,5))
    sns.countplot(x = "ANO_CMPT", data = dfNorte)      


    fig3 = plt.figure(figsize=(10,7))
    sns.set_palette("Accent")
    sns.set_style("darkgrid", {"grid.color": ".5", "grid.linestyle": ":"})
    ax = sns.lineplot(x='ANO_CMPT',y=dados['MORTE'] == 1, err_style="bars", errorbar=("se", 2), data=dfNorte2)
    ax.figure.set_size_inches(10,7)
    ax.set_title('Série temporal de mortes confirmadas',fontsize=20, fontweight="bold")

    fig4 = plt.figure(figsize=(10,7))
    ax2 = sns.lineplot(x='ANO_CMPT',y=dfSudesteAceleracao['Aceleração'] , data=dfNorteAceleracao)
    ax2.set_title('Velocidade de aceleração das mortes',fontsize=18)
    ax2.figure.set_size_inches(12,6)

    fig5 = plt.figure(figsize=(10,7))
    sns.set_palette("Accent")
    sns.set_style("darkgrid", {"grid.color": ".5", "grid.linestyle": ":"})
    ax = sns.lineplot(x='ANO_CMPT',y=dfSudesteAceleracao['media_movel'], data=dfNorteAceleracao)
    ax.figure.set_size_inches(12,6)
    ax.set_title('Média movel',fontsize=18) 
  
##############################################################################################################################################################  
  
Anos = ["Todo o periodo",2008,2015,2020]
    
Anos = st.sidebar.selectbox('Anos', Anos)   
    
if Anos == "Todo o periodo":
    Anos = ""
    
elif Anos == 2008 and regioes == "Sul":
        figu = plt.figure(figsize=(7,5))
        sns.countplot(x = "ANO_CMPT", data = dfSul2008)
    
elif Anos == 2015 and regioes == "Sul":
        figu = plt.figure(figsize=(7,5))
        sns.countplot(x = "ANO_CMPT", data = dfSul2015)   
        
elif Anos == 2020 and regioes == "Sul":
        figu = plt.figure(figsize=(7,5))
        sns.countplot(x = "ANO_CMPT", data = dfSul2020)      
##########################################################        
elif Anos == 2008 and regioes == "Sudeste":
        figu = plt.figure(figsize=(7,5))
        sns.countplot(x = "ANO_CMPT", data = dfSudeste2008)          
 
elif Anos == 2015 and regioes == "Sudeste":
        figu = plt.figure(figsize=(7,5))
        sns.countplot(x = "ANO_CMPT", data = dfSudeste2015)     
          
elif Anos == 2020 and regioes == "Sudeste":
        figu = plt.figure(figsize=(7,5))
        sns.countplot(x = "ANO_CMPT", data = dfSudeste2020)    
    
############################################################
elif Anos == 2008 and regioes == "Centro-oeste":
        figu = plt.figure(figsize=(7,5))
        sns.countplot(x = "ANO_CMPT", data = dfCentroOeste2008)
        
elif Anos == 2015 and regioes == "Centro-oeste":
        figu = plt.figure(figsize=(7,5))
        sns.countplot(x = "ANO_CMPT", data = dfCentroOeste2015)       
        
elif Anos == 2020 and regioes == "Centro-oeste":
        figu = plt.figure(figsize=(7,5))
        sns.countplot(x = "ANO_CMPT", data = dfCentroOeste2020)        
        
################################################################       
elif Anos == 2008 and regioes == "Nordeste":
        figu = plt.figure(figsize=(7,5))
        sns.countplot(x = "ANO_CMPT", data = dfNordeste2008)       
        
elif Anos == 2015 and regioes == "Nordeste":
        figu = plt.figure(figsize=(7,5))
        sns.countplot(x = "ANO_CMPT", data = dfNordeste2015)        
        
elif Anos == 2020 and regioes == "Nordeste":
        figu = plt.figure(figsize=(7,5))
        sns.countplot(x = "ANO_CMPT", data = dfNordeste2020)       
        
#######################################################################

elif Anos == 2008 and regioes == "Norte":
        figu = plt.figure(figsize=(7,5))
        sns.countplot(x = "ANO_CMPT", data = dfNorte2008)        
        
elif Anos == 2015 and regioes == "Norte":
        figu = plt.figure(figsize=(7,5))
        sns.countplot(x = "ANO_CMPT", data = dfNorte2015)      
        
        
elif Anos == 2020 and regioes == "Sul":
        figu = plt.figure(figsize=(7,5))
        sns.countplot(x = "ANO_CMPT", data = dfNorte2020)         
        
#################################################################################################################################################  
    
#ANO_CMPT = st.sidebar.checkbox('Dados de todo o periodo', value=True)


## Visaualizaçao no StreamLit

st.title('SÉRIE TEMPORAL')
col1,col2 = st.columns(2)

with col1:
            st.title('Contagem de mortes')
            st.pyplot(figu,use_container_width = True)
            st.pyplot(fig4,use_container_width = True)
       
        
with col2:
            st.pyplot(fig3,use_container_width = True)
            st.pyplot(fig5,use_container_width = True)
     
        
        
with st.container():
        st.dataframe(dados, hide_index=True)
        
        

url = 'https://youtu.be/xTaqY1KmHlw'

st.video(data = url)
    
    
st.divider()
st.markdown('Desenvolvido por **ALAN MOLTER** :technologist:')
st.divider()

contador = 1


if contador == 1:
        st.stop()
        
        




























