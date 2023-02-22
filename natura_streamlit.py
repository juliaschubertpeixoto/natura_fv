import streamlit as st

st.title("Projeto Berçário")

st.file_uploader("Selecione um arquivo", type='csv')

calculate = st.button("Calcular métricas")
if calculate:
    st.write("funcionou")
else:
    st.write('não clicou')