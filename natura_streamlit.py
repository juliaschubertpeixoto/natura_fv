import streamlit as st
import pandas as pd
import time

st.title("Projeto Berçário")

up_file = st.file_uploader("Selecione um arquivo", type=['csv', 'xlsx'], label_visibility='collapsed')

if up_file:
    df = pd.read_csv(up_file, encoding='utf8')
    st.success('Upload concluído!')
    st.subheader('Aplique seus filtros:')
    setor = st.text_input("Setor: ")
    grupo = st.text_input("Grupo: ")

    calculate = st.button("Calcular métricas")

    if calculate:
        with st.spinner('Calculando suas métricas'):
            time.sleep(2)
        st.success('Métricas calculadas com sucesso!', icon="✅")
        col1, col2, col3 = st.columns(3)
        with col1:
            if ((setor is not None) & (grupo is not None)):
                st.write(df)
                st.write('Colunas'+df.columns)
                bronze = df[(df['Setor']==setor) & (df['Grupo']==grupo) & (df['Nível']=='BRONZE')].count()/df[(df['Setor']==setor) & (df['Grupo']==grupo)].count()
                st.metric("Bronze", bronze)
        with col2:
            st.write('coluna 2')
        with col3:
            st.write('coluna 3')

    else:
        st.write('não clicou')