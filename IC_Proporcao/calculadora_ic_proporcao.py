#Importando bibliotecas
import numpy as np
from PIL import Image
import streamlit as st

#Indicando sidebar
st.markdown("<h1 style='font-size: 24px; color: black; font-weight: bold;'>Calculadora de Intervalo de Confiança de Proporção</h1>", unsafe_allow_html=True)

#Indicando do que se trata a web app
foto = Image.open('IC_Proporcao/bruno_carloto.jpg')
st.sidebar.image(foto, use_column_width=True, width=50)
st.sidebar.subheader('Bruno Rodrigues Carloto')
st.sidebar.markdown('Analista de dados e Política de Crédito')
st.sidebar.markdown('#### Projeto de Estatística Inferencial - IC para proporção')

st.sidebar.markdown("Redes Sociais :")
st.sidebar.markdown("- [Linkedin](https://www.linkedin.com/in/bruno-rodrigues-carloto)")
st.sidebar.markdown("- [Medium](https://medium.com/@brc-deep-analytics)")
st.sidebar.markdown("- [Mercadados](https://brunnocarlotosjob.wixsite.com/mercadados)")

tamanho_populacao = st.number_input("Insira o volume total da população, caso haja: ", min_value=0)
tamanho_amostra = st.number_input("Insira o volume total da amostra: ", min_value=0)
proporcao = st.number_input("Insira a proporção em forma decimal: ", min_value=0.0, max_value=1.0, step=0.0001)
confianca = st.selectbox('Selecione a o nível de confiança: ', ['99%', '95%', '90%'])


if tamanho_amostra == 0:
    st.write("")

elif tamanho_amostra > tamanho_populacao:
    st.write("ERRO: Amostra maior do que a população.")
    
else:
    st.markdown("<h1 style='font-size: 16px; color: gray; font-weight: bold;'>Resumo input</h1>", unsafe_allow_html=True)
    st.write(f'''
    * Volume população: {tamanho_populacao}
    
    * Volume amostra: {tamanho_amostra}
    
    * Proporção amostral: {proporcao * 100}%
    
    ''')
    # Calculando erro padrão
    erro_padrao = np.sqrt( ((proporcao * (1 - proporcao))/tamanho_amostra) )
    
    # Definições dos Z's
    Z_nivel_90 = 1.645
    Z_nivel_95 = 1.96
    Z_nivel_99 = 2.576

    if tamanho_populacao < 1:
        st.markdown("<h1 style='font-size: 16px; color: gray; font-weight: bold;'>Premissas de volume:</h1>", unsafe_allow_html=True)
        st.write("Volume populacional desconhecido.")
        
        # Buscando Zcrítico
        if confianca == '99%':
          ic_inferior = np.round(proporcao - Z_nivel_99 * erro_padrao, 4) * 100
          ic_superior = np.round(proporcao + Z_nivel_99 * erro_padrao, 4) * 100
          st.markdown("<h1 style='font-size: 16px; color: red; font-weight: bold;'>Resultado:</h1>", unsafe_allow_html=True)
          st.write(f"Com 99% de confiança, a proporção da população está entre {np.round(ic_inferior, 2)}% e {np.round(ic_superior, 2)}%.")
        
        elif confianca == '95%':
          ic_inferior = round(proporcao - Z_nivel_95 * erro_padrao, 4) * 100
          ic_superior = round(proporcao + Z_nivel_95 * erro_padrao, 4) * 100
          st.markdown("<h1 style='font-size: 16px; color: red; font-weight: bold;'>Resultado:</h1>", unsafe_allow_html=True)
          st.write(f"Com 95% de confiança, a proporção da população está entre {np.round(ic_inferior, 2)}% e {np.round(ic_superior, 2)}%.")
        
        elif confianca == '90%':
          ic_inferior = round(proporcao - Z_nivel_90 * erro_padrao, 4) * 100
          ic_superior = round(proporcao + Z_nivel_90 * erro_padrao, 4) * 100
          st.markdown("<h1 style='font-size: 16px; color: red; font-weight: bold;'>Resultado:</h1>", unsafe_allow_html=True)
          st.write(f"Com 90% de confiança, a proporção da população está entre {np.round(ic_inferior, 2)}% e {np.round(ic_superior, 2)}%.")
        
    else:
        infinitude_amostra = tamanho_amostra/tamanho_populacao

        if infinitude_amostra > 0.05:
            st.write("* População finita")
        
            # Análise de cumprimento das premissas de volumetria
            if (tamanho_amostra * proporcao >= 5) and (tamanho_amostra * (1 - proporcao) >= 5):
                st.markdown("<h1 style='font-size: 16px; color: gray; font-weight: bold;'>Premissas de volume:</h1>", unsafe_allow_html=True)
                st.write("Os números de sucesso e fracasso são suficientes para o cálculo.")
            
            
                # Buscando Zcrítico
                fator_correcao = np.sqrt((tamanho_populacao - tamanho_amostra)/(tamanho_populacao - 1))
                
                if confianca == '99%':
                  ic_inferior = np.round(proporcao - ((Z_nivel_99 * erro_padrao) * fator_correcao), 4) * 100
                  ic_superior = np.round(proporcao + ((Z_nivel_99 * erro_padrao) * fator_correcao), 4) * 100
                  st.markdown("<h1 style='font-size: 16px; color: red; font-weight: bold;'>Resultado:</h1>", unsafe_allow_html=True)
                  st.write(f"Com 99% de confiança, a proporção da população está entre {np.round(ic_inferior, 2)}% e {np.round(ic_superior, 2)}%.")
                
                
                elif confianca == '95%':
                  ic_inferior = round(proporcao - ((Z_nivel_95 * erro_padrao) * fator_correcao), 4) * 100
                  ic_superior = round(proporcao + ((Z_nivel_95 * erro_padrao) * fator_correcao), 4) * 100
                  st.markdown("<h1 style='font-size: 16px; color: red; font-weight: bold;'>Resultado:</h1>", unsafe_allow_html=True)
                  st.write(f"Com 95% de confiança, a proporção da população está entre {np.round(ic_inferior, 2)}% e {np.round(ic_superior, 2)}%.")
                
                elif confianca == '90%':
                  ic_inferior = round(proporcao - ((Z_nivel_90 * erro_padrao) * fator_correcao), 4) * 100
                  ic_superior = round(proporcao + ((Z_nivel_90 * erro_padrao) * fator_correcao), 4) * 100
                  st.markdown("<h1 style='font-size: 16px; color: red; font-weight: bold;'>Resultado:</h1>", unsafe_allow_html=True)
                  st.write(f"Com 90% de confiança, a proporção da população está entre {np.round(ic_inferior, 2)}% e {np.round(ic_superior, 2)}%.")
        
        else:
        
            st.write("* População infinita")
            
            # Análise de cumprimento das premissas de volumetria
            if (tamanho_amostra * proporcao >= 5) and (tamanho_amostra * (1 - proporcao) >= 5):
                st.markdown("<h1 style='font-size: 16px; color: gray; font-weight: bold;'>Premissas de volume:</h1>", unsafe_allow_html=True)
                st.write("Os números de sucesso e fracasso são suficientes para o cálculo.")

                if confianca == '99%':
                  ic_inferior = np.round(proporcao - (Z_nivel_99 * erro_padrao), 4) * 100
                  ic_superior = np.round(proporcao + (Z_nivel_99 * erro_padrao), 4) * 100
                  st.markdown("<h1 style='font-size: 16px; color: red; font-weight: bold;'>Resultado:</h1>", unsafe_allow_html=True)
                  st.write(f"Com 99% de confiança, a proporção da população está entre {np.round(ic_inferior, 2)}% e {np.round(ic_superior, 2)}%.")
                
                
                elif confianca == '95%':
                  ic_inferior = round(proporcao - (Z_nivel_95 * erro_padrao), 4) * 100
                  ic_superior = round(proporcao + (Z_nivel_95 * erro_padrao), 4) * 100
                  st.markdown("<h1 style='font-size: 16px; color: red; font-weight: bold;'>Resultado:</h1>", unsafe_allow_html=True)
                  st.write(f"Com 95% de confiança, a proporção da população está entre {np.round(ic_inferior, 2)}% e {np.round(ic_superior, 2)}%.")
                
                elif confianca == '90%':
                  ic_inferior = round(proporcao - (Z_nivel_90 * erro_padrao), 4) * 100
                  ic_superior = round(proporcao + (Z_nivel_90 * erro_padrao), 4) * 100
                  st.markdown("<h1 style='font-size: 16px; color: red; font-weight: bold;'>Resultado:</h1>", unsafe_allow_html=True)
                  st.write(f"Com 90% de confiança, a proporção da população está entre {np.round(ic_inferior, 2)}% e {np.round(ic_superior, 2)}%.")
        
    
            elif (tamanho_amostra * proporcao >= 5) and (tamanho_amostra * (1 - proporcao) < 5):
                st.markdown("<h1 style='font-size: 16px; color: gray; font-weight: bold;'>Premissas de volume:</h1>", unsafe_allow_html=True)
                st.write("PROBLEMA: O número de sucesso é suficiente para o cálculo, mas o número de fracasso não é. Ambos precisam ser.")
                
            elif (tamanho_amostra * proporcao < 5) and (tamanho_amostra * (1 - proporcao) >= 5):
                st.markdown("<h1 style='font-size: 16px; color: gray; font-weight: bold;'>Premissas de volume:</h1>", unsafe_allow_html=True)
                st.write("PROBLEMA: O número de fracasso é suficiente para o cálculo, mas o número de sucesso não é. Ambos precisam ser.")
                
            elif (tamanho_amostra * proporcao < 5) and (tamanho_amostra * (1 - proporcao) < 5):
                st.markdown("<h1 style='font-size: 16px; color: gray; font-weight: bold;'>Premissas de volume:</h1>", unsafe_allow_html=True)
                st.write("PROBLEMA: Os números de sucesso e fracasso NÃO são suficientes para o cálculo. Ambos precisam ser.")


