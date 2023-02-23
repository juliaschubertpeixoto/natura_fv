import streamlit as st
import pandas as pd
import time

st.title("Projeto Berçário")

up_file = st.file_uploader("Selecione um arquivo", type=['csv', 'xlsx'], label_visibility='collapsed')

if up_file:
    df = pd.read_csv(up_file, encoding='utf8', sep=';')
    df['Cd Consultora'] = df['Cd Consultora'].astype(int)
    df['Ciclo Início'] = df['Ciclo Início'].astype(int)
    df['Grupo'] = df['Grupo'].astype(int)

    st.success('Upload concluído!')
    choice = st.radio('Nível das métricas', ['Gerência', 'Setor', 'Grupo'])
    if choice=='Gerência':
        st.subheader('Digite sua gerência:')
        gerencia = str(st.text_input("Gerência: "))

    elif choice=='Setor':
        st.subheader('Digite seu setor:')
        setor = str(st.text_input("Setor: "))

    elif choice=='Grupo':
        st.subheader('Digite seu grupo:')
        setor = str(st.text_input("Grupo: "))
    
    st.subheader('Aplique seus filtros:')
    setor = str(st.text_input("Setor: "))
    grupo = str(st.number_input("Grupo: "))

    calculate = st.button("Calcular métricas")

    if calculate:
        with st.spinner('Calculando suas métricas'):
            time.sleep(0.5)
        st.success('Métricas calculadas com sucesso!', icon="✅")
        col1, col2, col3 = st.columns(3)
        with col1:
            if ((setor is not None) & (grupo is not None)):
                st.write(setor)
                st.write(grupo)
                st.write(df[(df['Setor']=='CORAÇÃO GAÚCHO') & (df['Grupo']==9146) & (df['Nível']=='BRONZE')]['Cd Consultora'].count())
                st.write(df[(df['Setor']==setor) & (df['Grupo']==grupo)]['Cd Consultora'].count())
                st.metric("Bronze", 10)
    else:
        st.write('não clicou')