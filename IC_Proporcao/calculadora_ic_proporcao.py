# Importando bibliotecas
import numpy as np
from PIL import Image
import streamlit as st

# Apresentação da ferramenta
st.markdown("<h1 style='font-size: 24px; color: black; font-weight: bold;'>Calculadora de Intervalo de Confiança de Proporção</h1>", unsafe_allow_html=True)

# Informações pessoais e objetivo do projeto
foto = Image.open('IC_Proporcao/bruno_carloto.jpg')
st.sidebar.image(foto, use_column_width=True, width=50)
st.sidebar.subheader('Bruno Rodrigues Carloto')
st.sidebar.markdown('Analista de dados e Política de Crédito')
st.sidebar.markdown('#### Projeto de Estatística Inferencial - IC para proporção')
st.sidebar.markdown("Redes Sociais :")
st.sidebar.markdown("- [Linkedin](https://www.linkedin.com/in/bruno-rodrigues-carloto)")
st.sidebar.markdown("- [Medium](https://medium.com/@brc-deep-analytics)")
st.sidebar.markdown("- [Mercadados](https://brunnocarlotosjob.wixsite.com/mercadados)")

# Seleção de página
st.sidebar.markdown("<h1 style='font-size: 18px; color: gray; font-weight: bold;'>Página:</h1>", unsafe_allow_html=True)
pagina = st.sidebar.selectbox("", ["1. Calculadora", "2. Breve teoria"])

if pagina == "1. Calculadora":
    
    # Input das informações para inferência do intervalo de confiança
    tamanho_populacao = st.number_input("Insira o volume total da população, caso haja: ", min_value=0)
    tamanho_amostra = st.number_input("Insira o volume total da amostra: ", min_value=0)
    proporcao = st.number_input("Insira a proporção em forma decimal: ", min_value=0.0, max_value=1.0, step=0.0001)
    confianca = st.selectbox('Selecione a o nível de confiança: ', ['99%', '95%', '90%'])
    
    # Condição para manter a página limpa enquanto não se passa informação da amostra
    if tamanho_amostra == 0:
        st.write("")
    
    # Sinalizando quando a amostra for maior do que a população, pois denota incoerência
    elif tamanho_amostra > tamanho_populacao:
        st.write("ERRO: Amostra maior do que a população.")
    
    # Não havendo erro iniciamos a etapa de geração do intervalo   
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
    
        # Quando a população é desconhecida, informamos e calculamos o intervalo de confiança
        if tamanho_populacao < 1:
            st.markdown("<h1 style='font-size: 16px; color: gray; font-weight: bold;'>Premissas de volume:</h1>", unsafe_allow_html=True)
            st.write("Volume populacional desconhecido.")
        
        # ------------------------------- Cálculos dos intervalos ------------------------------
    
            # Nível de confiança 99%
            if confianca == '99%':
              ic_inferior = np.round(proporcao - Z_nivel_99 * erro_padrao, 4) * 100
              ic_superior = np.round(proporcao + Z_nivel_99 * erro_padrao, 4) * 100
              st.markdown("<h1 style='font-size: 16px; color: red; font-weight: bold;'>Resultado:</h1>", unsafe_allow_html=True)
              st.write(f"Com 99% de confiança, a proporção da população está entre {np.round(ic_inferior, 2)}% e {np.round(ic_superior, 2)}%.")
            
            # Nível de confiança 95%
            elif confianca == '95%':
              ic_inferior = round(proporcao - Z_nivel_95 * erro_padrao, 4) * 100
              ic_superior = round(proporcao + Z_nivel_95 * erro_padrao, 4) * 100
              st.markdown("<h1 style='font-size: 16px; color: red; font-weight: bold;'>Resultado:</h1>", unsafe_allow_html=True)
              st.write(f"Com 95% de confiança, a proporção da população está entre {np.round(ic_inferior, 2)}% e {np.round(ic_superior, 2)}%.")
            
            # Nível de confiança 90%
            elif confianca == '90%':
              ic_inferior = round(proporcao - Z_nivel_90 * erro_padrao, 4) * 100
              ic_superior = round(proporcao + Z_nivel_90 * erro_padrao, 4) * 100
              st.markdown("<h1 style='font-size: 16px; color: red; font-weight: bold;'>Resultado:</h1>", unsafe_allow_html=True)
              st.write(f"Com 90% de confiança, a proporção da população está entre {np.round(ic_inferior, 2)}% e {np.round(ic_superior, 2)}%.")
    
        # Quando a população é conhecida, calculamos a finitude da população e calculamos o intervalo de confiança    
        else:
    
            # Calculando a finitude da população
            infinitude_populacao = tamanho_amostra/tamanho_populacao
    
            # Quando a população é finita aplicamos fator de erro
            if infinitude_populacao > 0.05:
                st.write("* População finita")
            
                # Análise de cumprimento das premissas de volumetria
                if (tamanho_amostra * proporcao >= 5) and (tamanho_amostra * (1 - proporcao) >= 5):
                    st.markdown("<h1 style='font-size: 16px; color: gray; font-weight: bold;'>Premissas de volume:</h1>", unsafe_allow_html=True)
                    st.write("Os números de sucesso e fracasso são suficientes para o cálculo.")
                
                
                    # Calculando fator de correção
                    fator_correcao = np.sqrt((tamanho_populacao - tamanho_amostra)/(tamanho_populacao - 1))
                    
                    # Intervalo de confiança de 99% com fator de correção
                    if confianca == '99%':
                      ic_inferior = np.round(proporcao - ((Z_nivel_99 * erro_padrao) * fator_correcao), 4) * 100
                      ic_superior = np.round(proporcao + ((Z_nivel_99 * erro_padrao) * fator_correcao), 4) * 100
                      st.markdown("<h1 style='font-size: 16px; color: red; font-weight: bold;'>Resultado:</h1>", unsafe_allow_html=True)
                      st.write(f"Com 99% de confiança, a proporção da população está entre {np.round(ic_inferior, 2)}% e {np.round(ic_superior, 2)}%.")
                    
                    # Intervalo de confiança de 95% com fator de correção
                    elif confianca == '95%':
                      ic_inferior = round(proporcao - ((Z_nivel_95 * erro_padrao) * fator_correcao), 4) * 100
                      ic_superior = round(proporcao + ((Z_nivel_95 * erro_padrao) * fator_correcao), 4) * 100
                      st.markdown("<h1 style='font-size: 16px; color: red; font-weight: bold;'>Resultado:</h1>", unsafe_allow_html=True)
                      st.write(f"Com 95% de confiança, a proporção da população está entre {np.round(ic_inferior, 2)}% e {np.round(ic_superior, 2)}%.")
                    
                    # Intervalo de confiança de 90% com fator de correção
                    elif confianca == '90%':
                      ic_inferior = round(proporcao - ((Z_nivel_90 * erro_padrao) * fator_correcao), 4) * 100
                      ic_superior = round(proporcao + ((Z_nivel_90 * erro_padrao) * fator_correcao), 4) * 100
                      st.markdown("<h1 style='font-size: 16px; color: red; font-weight: bold;'>Resultado:</h1>", unsafe_allow_html=True)
                      st.write(f"Com 90% de confiança, a proporção da população está entre {np.round(ic_inferior, 2)}% e {np.round(ic_superior, 2)}%.")
    
                # ------------------ Análise de cumprimento das premissas de volumetria -----------------------
                
                elif (tamanho_amostra * proporcao >= 5) and (tamanho_amostra * (1 - proporcao) < 5):
                    st.markdown("<h1 style='font-size: 16px; color: gray; font-weight: bold;'>Premissas de volume:</h1>", unsafe_allow_html=True)
                    st.write("PROBLEMA: O número de sucesso é suficiente para o cálculo, mas o número de fracasso não é. Ambos precisam ser.")
                    
                elif (tamanho_amostra * proporcao < 5) and (tamanho_amostra * (1 - proporcao) >= 5):
                    st.markdown("<h1 style='font-size: 16px; color: gray; font-weight: bold;'>Premissas de volume:</h1>", unsafe_allow_html=True)
                    st.write("PROBLEMA: O número de fracasso é suficiente para o cálculo, mas o número de sucesso não é. Ambos precisam ser.")
                    
                elif (tamanho_amostra * proporcao < 5) and (tamanho_amostra * (1 - proporcao) < 5):
                    st.markdown("<h1 style='font-size: 16px; color: gray; font-weight: bold;'>Premissas de volume:</h1>", unsafe_allow_html=True)
                    st.write("PROBLEMA: Os números de sucesso e fracasso NÃO são suficientes para o cálculo. Ambos precisam ser.")
    
                else:
                    st.write('Falha')
           
            # Em casos de população infinita
            else:
            
                st.write("* População infinita")
                
                # Análise de cumprimento das premissas de volumetria
                if (tamanho_amostra * proporcao >= 5) and (tamanho_amostra * (1 - proporcao) >= 5):
                    st.markdown("<h1 style='font-size: 16px; color: gray; font-weight: bold;'>Premissas de volume:</h1>", unsafe_allow_html=True)
                    st.write("Os números de sucesso e fracasso são suficientes para o cálculo.")
    
                    # Intervalo de confiança de 99% com fator de correção
                    if confianca == '99%':
                      ic_inferior = np.round(proporcao - (Z_nivel_99 * erro_padrao), 4) * 100
                      ic_superior = np.round(proporcao + (Z_nivel_99 * erro_padrao), 4) * 100
                      st.markdown("<h1 style='font-size: 16px; color: red; font-weight: bold;'>Resultado:</h1>", unsafe_allow_html=True)
                      st.write(f"Com 99% de confiança, a proporção da população está entre {np.round(ic_inferior, 2)}% e {np.round(ic_superior, 2)}%.")
                    
                    # Intervalo de confiança de 95% com fator de correção
                    elif confianca == '95%':
                      ic_inferior = round(proporcao - (Z_nivel_95 * erro_padrao), 4) * 100
                      ic_superior = round(proporcao + (Z_nivel_95 * erro_padrao), 4) * 100
                      st.markdown("<h1 style='font-size: 16px; color: red; font-weight: bold;'>Resultado:</h1>", unsafe_allow_html=True)
                      st.write(f"Com 95% de confiança, a proporção da população está entre {np.round(ic_inferior, 2)}% e {np.round(ic_superior, 2)}%.")
                    
                    # Intervalo de confiança de 90% com fator de correção
                    elif confianca == '90%':
                      ic_inferior = round(proporcao - (Z_nivel_90 * erro_padrao), 4) * 100
                      ic_superior = round(proporcao + (Z_nivel_90 * erro_padrao), 4) * 100
                      st.markdown("<h1 style='font-size: 16px; color: red; font-weight: bold;'>Resultado:</h1>", unsafe_allow_html=True)
                      st.write(f"Com 90% de confiança, a proporção da população está entre {np.round(ic_inferior, 2)}% e {np.round(ic_superior, 2)}%.")
            
                # ------------------ Análise de cumprimento das premissas de volumetria -----------------------
    
                elif (tamanho_amostra * proporcao >= 5) and (tamanho_amostra * (1 - proporcao) < 5):
                    st.markdown("<h1 style='font-size: 16px; color: gray; font-weight: bold;'>Premissas de volume:</h1>", unsafe_allow_html=True)
                    st.write("PROBLEMA: O número de sucesso é suficiente para o cálculo, mas o número de fracasso não é. Ambos precisam ser.")
                    
                elif (tamanho_amostra * proporcao < 5) and (tamanho_amostra * (1 - proporcao) >= 5):
                    st.markdown("<h1 style='font-size: 16px; color: gray; font-weight: bold;'>Premissas de volume:</h1>", unsafe_allow_html=True)
                    st.write("PROBLEMA: O número de fracasso é suficiente para o cálculo, mas o número de sucesso não é. Ambos precisam ser.")
                    
                elif (tamanho_amostra * proporcao < 5) and (tamanho_amostra * (1 - proporcao) < 5):
                    st.markdown("<h1 style='font-size: 16px; color: gray; font-weight: bold;'>Premissas de volume:</h1>", unsafe_allow_html=True)
                    st.write("PROBLEMA: Os números de sucesso e fracasso NÃO são suficientes para o cálculo. Ambos precisam ser.")

elif pagina == "2. Breve teoria":

    st.write("Hello, world!")
