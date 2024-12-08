# Importando bibliotecas
import numpy as np
from PIL import Image
import streamlit as st

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

    # Apresentação da ferramenta
    st.markdown("<h1 style='font-size: 24px; color: black; font-weight: bold;'>Calculadora de Intervalo de Confiança de Proporção</h1>", unsafe_allow_html=True)
    
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

    # Apresentação da ferramenta
    st.markdown("<h1 style='font-size: 24px; color: black; font-weight: bold;'>Breve contexto</h1>", unsafe_allow_html=True)
    st.write('''
    Este projeto surgiu da proatividade frente à necessidade da aplicação da Estatística Inferencial no cenário de Política de Crédito, 
    quando buscamos identificar a inadimplência de uma população público-alvo com determinada característica (score, comportamento, cadastrais etc.), 
    acerca da qual não temos performance para a todalidade, mas temos para uma proporção dela.

    A partir da inadimplência de uma amostra, 
    podemos generalizar a mesma para a população, entendendo estatisticamente o nível de risco da totalidade desse público.
    ''')
    st.markdown("<h1 style='font-size: 24px; color: black; font-weight: bold;'>Breve teoria</h1>", unsafe_allow_html=True)
    st.write('''
    A Estatística Inferencial é justamente, a partir de uma amostra, generalizarmos determinada estatística/proporção/probabilidade a uma população
    que não temos acesso.

    Exemplos:

    * A partir de uma amostra, inferirmos a inadimplência de uma população;
    * A partir de uma amostra, inferirmos a proporção de votos de um candidato a nível populacional;
    * A partir de uma amostra, inferirmos a proporção de peças de uma produção estar danificada.
    ''')
    st.markdown("<h1 style='font-size: 20px; color: black; font-weight: bold;'>Premissas</h1>", unsafe_allow_html=True)
    st.write('''
    1. __*n.p >= 5*__
    2. __*n.q >= 5*__

    onde:

    * *n*: tamanho da amostra
    * *p*: proporção de sucesso
    * *q*: proporção de fracasso | (1 - p)
    ''')
    st.markdown("<h1 style='font-size: 20px; color: black; font-weight: bold;'>Fórmulas</h1>", unsafe_allow_html=True)
    st.write('''
    Há basicamente duas fórmulas, uma para quando a população é finita e outra para quando é infinita.
    ''')
    st.markdown("<h1 style='font-size: 14px; color: black; font-weight: bold;'>População finita</h1>", unsafe_allow_html=True)
    st.write('''
    A população é finita quando:
    ''')

    # Definição e plotagem da imagem do cálculo de população finita
    foto_pop_finita = Image.open('IC_Proporcao/pop_finita.png')
    dim_foto_pop_finita = (100,50)
    foto_pop_finita = foto_pop_finita.resize(dim_foto_pop_finita)
    st.image(foto_pop_finita)
    
    st.write('''
    Nesse caso, usa-se a seguinte fórmula:
    ''')

    # Definição e plotagem da imagem do cálculo de IC com população finita
    foto_ic_com_fator_correcao = Image.open('IC_Proporcao/ic_com_fator_correcao.jpg')
    dim_foto_ic_com_fator_correcao = (250,90)
    foto_ic_com_fator_correcao = foto_ic_com_fator_correcao.resize(dim_foto_ic_com_fator_correcao)
    st.image(foto_ic_com_fator_correcao)
    
