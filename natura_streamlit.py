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
    with st.spinner('Calculando suas métricas'):
        time.sleep(2)
    st.success('Métricas calculadas com sucesso!', icon="✅")

    if calculate:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write('coluna 1')
        with col2:
            st.write('coluna 2')
        with col3:
            st.write('coluna 3')

    else:
        st.write('não clicou')