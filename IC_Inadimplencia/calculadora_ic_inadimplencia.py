#Importando bibliotecas
import numpy as np
from PIL import Image
import streamlit as st

#Indicando sidebar
st.markdown('*__Observação: para mais informações acerca do projeto, clique na seta no canto esquerdo superior da tela__* ')

#Indicando do que se trata a web app
foto = Image.open('bruno.carloto (2).png')
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

usuario =  st.text_input('Me informe seu nome para termos uma interação melhor.')
renda = st.number_input('Me informe sua renda.')
parcela = st.radio('Selecione a quantidade de parcela',(1, 2, 3, 4, 5))
st.write('Valor à vista se o empréstimo for aprovado: R$ {} por mês'.format(mensalidade))
if st.button("Ver Resultado"):
