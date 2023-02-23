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
    st.subheader('Aplique seus filtros:')
    setor = str(st.text_input("Setor: "))
    grupo = str(st.text_input("Grupo: "))

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
                st.write(df[(df['Setor']==setor) & (df['Grupo']==grupo) & (df['Nível']=='BRONZE')]['Cd Consultora'].count())
                st.write(df[(df['Setor']==setor) & (df['Grupo']==grupo)]['Cd Consultora'].count())
                bronze = ((df[(df['Setor']==setor) & (df['Grupo']==grupo) & (df['Nível']=='BRONZE')]['Cd Consultora'].count())/(df[(df['Setor']==setor) & (df['Grupo']==grupo)]['Cd Consultora'].count()))
                st.metric("Bronze", bronze)
    else:
        st.write('não clicou')