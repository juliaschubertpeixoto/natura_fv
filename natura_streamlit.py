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
        #st.subheader('Digite sua gerência:')
        #gerencia = str(st.text_input("Gerência: "))
        bronze = ((df[df['Nível']=='BRONZE']['Cd Consultora'].count())/(df['Cd Consultora'].count())*100)
        prata = ((df[df['Nível']=='PRATA']['Cd Consultora'].count())/(df['Cd Consultora'].count())*100)
        ouro = ((df[df['Nível']=='OURO']['Cd Consultora'].count())/(df['Cd Consultora'].count())*100)
        ativa = ((df[df['Status CN']=='ATIVA']['Cd Consultora'].count())/(df['Cd Consultora'].count())*100)
        digital = ((df[df['Venda Digital']=='SIM']['Cd Consultora'].count())/(df['Cd Consultora'].count())*100)
        treinamento = ((df[df['Treinamento']=='SIM']['Cd Consultora'].count())/(df['Cd Consultora'].count())*100)
        debito = ((df[df['Débito']=='SIM']['Cd Consultora'].count())/(df['Cd Consultora'].count())*100)
        status = ['I4', 'I5', 'I6']
        indisp = ((df[df['Status CN'].isin(status)]['Cd Consultora'].count())/(df['Cd Consultora'].count())*100)
        itres = ((df[df['Status CN']=='I3']['Cd Consultora'].count())/(df['Cd Consultora'].count())*100)

    elif choice=='Setor':
        st.subheader('Digite seu setor:')
        setor = str(st.text_input("Setor: "))
        bronze = ((df[(df['Nível']=='BRONZE') & (df['Setor']==setor)]['Cd Consultora'].count())/(df[df['Setor']==setor]['Cd Consultora'].count())*100)
        prata = ((df[(df['Nível']=='PRATA') & (df['Setor']==setor)]['Cd Consultora'].count())/(df[df['Setor']==setor]['Cd Consultora'].count())*100)
        ouro = ((df[(df['Nível']=='OURO') & (df['Setor']==setor)]['Cd Consultora'].count())/(df[df['Setor']==setor]['Cd Consultora'].count())*100)
        ativa = ((df[(df['Status CN']=='ATIVA') & (df['Setor']==setor)]['Cd Consultora'].count())/(df[df['Setor']==setor]['Cd Consultora'].count())*100)
        digital = ((df[(df['Venda Digital']=='SIM') & (df['Setor']==setor)]['Cd Consultora'].count())/(df[df['Setor']==setor]['Cd Consultora'].count())*100)
        treinamento = ((df[(df['Treinamento']=='SIM') & (df['Setor']==setor)]['Cd Consultora'].count())/(df[df['Setor']==setor]['Cd Consultora'].count())*100)
        debito = ((df[(df['Débito']=='SIM') & (df['Setor']==setor)]['Cd Consultora'].count())/(df[df['Setor']==setor]['Cd Consultora'].count())*100)
        status = ['I4', 'I5', 'I6']
        indisp = ((df[(df['Status CN'].isin(status)) & (df['Setor']==setor)]['Cd Consultora'].count())/(df[df['Setor']==setor]['Cd Consultora'].count())*100)
        itres = ((df[(df['Status CN']=='I3') & (df['Setor']==setor)]['Cd Consultora'].count())/(df[df['Setor']==setor]['Cd Consultora'].count())*100)

    elif choice=='Grupo':
        st.subheader('Digite seu grupo:')
        grupo = st.text_input("Grupo: ")
        bronze = ((df[(df['Nível']=='BRONZE') & (df['Grupo']==grupo)]['Cd Consultora'].count())/(df[df['Grupo']==grupo]['Cd Consultora'].count())*100)
        prata = ((df[(df['Nível']=='PRATA') & (df['Grupo']==grupo)]['Cd Consultora'].count())/(df[df['Grupo']==grupo]['Cd Consultora'].count())*100)
        ouro = ((df[(df['Nível']=='OURO') & (df['Grupo']==grupo)]['Cd Consultora'].count())/(df[df['Grupo']==grupo]['Cd Consultora'].count())*100)
        ativa = ((df[(df['Status CN']=='ATIVA') & (df['Grupo']==grupo)]['Cd Consultora'].count())/(df[df['Grupo']==grupo]['Cd Consultora'].count())*100)
        digital = ((df[(df['Venda Digital']=='SIM') & (df['Grupo']==grupo)]['Cd Consultora'].count())/(df[df['Grupo']==grupo]['Cd Consultora'].count())*100)
        treinamento = ((df[(df['Treinamento']=='SIM') & (df['Grupo']==grupo)]['Cd Consultora'].count())/(df[df['Grupo']==grupo]['Cd Consultora'].count())*100)
        debito = ((df[(df['Débito']=='SIM') & (df['Grupo']==grupo)]['Cd Consultora'].count())/(df[df['Grupo']==grupo]['Cd Consultora'].count())*100)
        status = ['I4', 'I5', 'I6']
        indisp = ((df[(df['Status CN'].isin(status)) & (df['Grupo']==grupo)]['Cd Consultora'].count())/(df[df['Grupo']==grupo]['Cd Consultora'].count())*100)
        itres = ((df[(df['Status CN']=='I3') & (df['Grupo']==grupo)]['Cd Consultora'].count())/(df[df['Grupo']==grupo]['Cd Consultora'].count())*100)

    calculate = st.button("Calcular métricas")

    if calculate:
        with st.spinner('Calculando as métricas...'):
            time.sleep(0.2)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Bronze", f"{bronze:.1f}%")
            st.metric("Ativas", f"{ativa:.1f}%")
            st.metric("Débito", f"{debito:.1f}%")
        with col2:
            st.metric("Prata", f"{prata:.1f}%")
            st.metric("Digitalização", f"{digital:.1f}%")
            st.metric("Indisponíveis", f"{indisp:.1f}%")
        with col3:
            st.metric("Ouro", f"{ouro:.1f}%")
            st.metric("Treinamento", f"{treinamento:.1f}%")
            st.metric("i3", f"{itres:.1f}%")

    else:
        st.write('Clique no botão para calcular as métricas')