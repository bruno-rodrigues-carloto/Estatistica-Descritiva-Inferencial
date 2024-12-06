#Importando bibliotecas
import numpy as np
from PIL import Image
import streamlit as st

#Indicando sidebar
st.markdown("<h1 style='font-size: 24px; color: black; font-weight: bold;'>Calculadora de Intervalo de Confiança de inadimplentes</h1>", unsafe_allow_html=True)

#Indicando do que se trata a web app
# foto = Image.open('bruno.carloto (2).png')
# st.sidebar.image(foto, use_column_width=True)
st.sidebar.subheader('Bruno Rodrigues Carloto')
st.sidebar.markdown('Analista de dados')
st.sidebar.markdown('#### Projeto de portfólio de Ciência de Dados')
st.sidebar.markdown('''Leia o [artigo do projeto](https://br-cienciadedados.medium.com/projeto-de-machine-learning-ii-9c889faec8df), o qual descreve o passo a passo
do desenvolvimento do modelo de machine learning. As descrições vão desde a limpeza dos dados até à análise do desempenho dos modelos e a seleção do melhor.''')
st.sidebar.title('Menu')
pag = st.sidebar.selectbox('Selecione a página', ['Interagir com a inteligência', 'Dashboard da base de dados do projeto'])

st.sidebar.markdown('Feito por : Bruno Rodrigues Carloto')

st.sidebar.markdown("Redes Sociais :")
st.sidebar.markdown("- [Linkedin](https://www.linkedin.com/in/bruno-rodrigues-carloto)")
st.sidebar.markdown("- [Medium](https://medium.com/@brc-deep-analytics)")
st.sidebar.markdown("- [Mercadados](https://brunnocarlotosjob.wixsite.com/mercadados)")

tamanho_amostra = st.number_input("Insira o volume total da amostra: ", min_value=0)
tamanho_amostra_convertido = st.number_input("Insira o volume total da amostra convertida no Positivo: ", min_value=0)
inad_positivo = st.number_input("Insira a inadimplência Positivo: ", min_value=0.0, max_value=1.0, step=0.0001)
confianca = st.selectbox('Selecione a página', ['99%', '95%', '90%'])

# Calculando erro padrão para margem de erro
if tamanho_amostra_convertido == 0:
    st.write("")
    
else:
    st.markdown("<h1 style='font-size: 16px; color: gray; font-weight: bold;'>Resumo input</h1>", unsafe_allow_html=True)
    st.write(f'''
    Volume amostral: {tamanho_amostra}
    
    Volume amostral convertido: {tamanho_amostra_convertido}
    
    Inadimplência amostral convertido: {inad_positivo * 100}%
    
    ''')
    # Calculando erro padrão
    erro_padrao = np.sqrt( ((inad_positivo * (1 - inad_positivo))/tamanho_amostra_convertido) )
    
    # Definições dos Z's
    Z_nivel_90 = 1.645
    Z_nivel_95 = 1.96
    Z_nivel_99 = 2.576

        # Análise de cumprimento das premissas de volumetria
    if (tamanho_amostra_convertido * inad_positivo >= 10) and (tamanho_amostra_convertido * (1 - inad_positivo) >= 10):
        st.markdown("<h1 style='font-size: 16px; color: gray; font-weight: bold;'>Premissas de volume:</h1>", unsafe_allow_html=True)
        st.write("Os números de inadimplentes e adimplentes são suficientes para o cálculo.")
        
    elif (tamanho_amostra_convertido * inad_positivo >= 10) and (tamanho_amostra_convertido * (1 - inad_positivo) < 10):
        st.markdown("<h1 style='font-size: 16px; color: gray; font-weight: bold;'>Premissas de volume:</h1>", unsafe_allow_html=True)
        st.write("O número de inadimplentes é suficiente para o cálculo, mas o número de adimplentes não é.")
        
    elif (tamanho_amostra_convertido * inad_positivo < 10) and (tamanho_amostra_convertido * (1 - inad_positivo) >= 10):
        st.markdown("<h1 style='font-size: 16px; color: gray; font-weight: bold;'>Premissas de volume:</h1>", unsafe_allow_html=True)
        st.write("O número de adimplentes é suficiente para o cálculo, mas o número de inadimplentes não é.")
        
    elif (tamanho_amostra_convertido * inad_positivo < 10) and (tamanho_amostra_convertido * (1 - inad_positivo) < 10):
        st.markdown("<h1 style='font-size: 16px; color: gray; font-weight: bold;'>Premissas de volume:</h1>", unsafe_allow_html=True)
        st.write("Os números de inadimplentes e adimplentes NÃO são suficientes para o cálculo.")
    
    
    # Buscando Zcrítico
    if confianca == '99%':
      ic_inferior = np.round(inad_positivo - Z_nivel_99 * erro_padrao, 4) * 100
      ic_superior = np.round(inad_positivo + Z_nivel_99 * erro_padrao, 4) * 100
      st.markdown("<h1 style='font-size: 16px; color: red; font-weight: bold;'>Resultado:</h1>", unsafe_allow_html=True)
      st.write(f"Com 99% de confiança, a indimplência da população está entre {np.round(ic_inferior, 2)}% e {np.round(ic_superior, 2)}%.")
    
    
    elif confianca == '95%':
      ic_inferior = round(inad_positivo - Z_nivel_95 * erro_padrao, 4) * 100
      ic_superior = round(inad_positivo + Z_nivel_95 * erro_padrao, 4) * 100
      st.markdown("<h1 style='font-size: 16px; color: red; font-weight: bold;'>Resultado:</h1>", unsafe_allow_html=True)
      st.write(f"Com 95% de confiança, a indimplência da população está entre {np.round(ic_inferior, 2)}% e {np.round(ic_superior, 2)}%.")
    
    elif confianca == '90%':
      ic_inferior = round(inad_positivo - Z_nivel_90 * erro_padrao, 4) * 100
      ic_superior = round(inad_positivo + Z_nivel_90 * erro_padrao, 4) * 100
      st.markdown("<h1 style='font-size: 16px; color: red; font-weight: bold;'>Resultado:</h1>", unsafe_allow_html=True)
      st.write(f"Com 90% de confiança, a indimplência da população está entre {np.round(ic_inferior, 2)}% e {np.round(ic_superior, 2)}%.")

