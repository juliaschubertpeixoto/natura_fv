import streamlit as st

st.title("Projeto Berçário")

up_file = st.file_uploader("Selecione um arquivo", type='csv')

if up_file is not None:

    calculate = st.button("Calcular métricas")
    if calculate:
        st.write("Métricas")
    else:
        st.write('não clicou')