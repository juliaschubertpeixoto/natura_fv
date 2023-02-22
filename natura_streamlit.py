import streamlit as st

st.title("Projeto Berçário")

up_file = st.file_uploader("Selecione um arquivo", type=['csv', 'xlsx'])

if up_file is not None:
    df = pd.read_csv(up_file)
    with st.spinner('Fazendo upload do arquivo'):
        time.sleep(5)
    st.success('Upload concluído!')
    st.subheader('Aplique seus filtros:')
    setor = st.text_input("Setor: ")
    grupo = st.text_input("Grupo: ")

    calculate = st.button("Calcular métricas")

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