import streamlit as st
import pandas as pd
import numpy as np
import time

st.title("Projeto Berçário")

up_file = st.file_uploader("Selecione um arquivo", type=['csv', 'xlsx'])

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
        st.subheader('Digite ou selecione o setor:')
        setor = str(st.selectbox("Setor: ", options=np.sort(df["Setor"].unique()), help="Digite ou selecione o grupo"))
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
        st.subheader('Digite ou selecione o grupo:')
        grupo_values = np.sort(df["Grupo"].unique())
        grupo = st.selectbox("Grupo: ", options=grupo_values[grupo_values > 0], help="Digite ou selecione o grupo")
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
            st.metric(label="Bronze",value=f"{bronze:.1f}%")
            if bronze>30:
                potencial = '<b><p style="color:green">Alto Potencial de Desenvolvimento</p></b>'
                st.markdown(potencial, unsafe_allow_html=True)
            elif bronze<20:
                potencial = '<b><p style="color:red">Alerta Plano de \n Crescimento</p></b>'
                st.markdown(potencial, unsafe_allow_html=True)
            else:
                st.write("Médio Potencial de Desenvolvimento")
            st.metric("Ativas", f"{ativa:.1f}%")
            if ativa>50:
                potencial = '<b><p style="color:green">Alto Potencial de Desenvolvimento</p></b>'
                st.markdown(potencial, unsafe_allow_html=True)
            elif ativa<20:
                potencial = '<b><p style="color:red">Alerta Plano de Crescimento</p></b>'
                st.markdown(potencial, unsafe_allow_html=True)
            else:
                st.write("Médio Potencial de Desenvolvimento")
            st.metric("Débito", f"{debito:.1f}%")
            if debito<10:
                potencial = '<b><p style="color:green">Alto Potencial de Desenvolvimento</p></b>'
                st.markdown(potencial, unsafe_allow_html=True)
            elif debito>20:
                potencial = '<b><p style="color:red">Alerta Plano de Crescimento</p></b>'
                st.markdown(potencial, unsafe_allow_html=True)
            else:
                st.write("Médio Potencial de Desenvolvimento")
        with col2:
            st.metric("Prata", f"{prata:.1f}%")
            if prata>25:
                potencial = '<b><p style="color:green">Alto Potencial de Desenvolvimento</p></b>'
                st.markdown(potencial, unsafe_allow_html=True)
            elif prata<10:
                potencial = '<b><p style="color:red">Alerta Plano de Crescimento</p></b>'
                st.markdown(potencial, unsafe_allow_html=True)
            else:
                st.write("Médio Potencial de Desenvolvimento")
            st.metric("Digitalização", f"{digital:.1f}%")
            if digital>75:
                potencial = '<b><p style="color:green">Alto Potencial de Desenvolvimento</p></b>'
                st.markdown(potencial, unsafe_allow_html=True)
            elif digital<50:
                potencial = '<b><p style="color:red">Alerta Plano de Crescimento</p></b>'
                st.markdown(potencial, unsafe_allow_html=True)
            else:
                st.write("Médio Potencial de Desenvolvimento")
            st.metric("Indisponíveis", f"{indisp:.1f}%")
            if indisp<15:
                potencial = '<b><p style="color:green">Alto Potencial de Desenvolvimento</p></b>'
                st.markdown(potencial, unsafe_allow_html=True)
            elif indisp>25:
                potencial = '<b><p style="color:red">Alerta Plano de Crescimento</p></b>'
                st.markdown(potencial, unsafe_allow_html=True)
            else:
                st.write("Médio Potencial de Desenvolvimento")
        with col3:
            st.metric("Ouro", f"{ouro:.1f}%")
            if ouro>10:
                potencial = '<b><p style="color:green">Alto Potencial de Desenvolvimento</p></b>'
                st.markdown(potencial, unsafe_allow_html=True)
            elif ouro<5:
                potencial = '<b><p style="color:red">Alerta Plano de Crescimento</p></b>'
                st.markdown(potencial, unsafe_allow_html=True)
            else:
                st.write("Médio Potencial de Desenvolvimento")
            st.metric("Treinamento", f"{treinamento:.1f}%")
            if treinamento>80:
                potencial = '<b><p style="color:green">Alto Potencial de Desenvolvimento</p></b>'
                st.markdown(potencial, unsafe_allow_html=True)
            elif treinamento<40:
                potencial = '<b><p style="color:red">Alerta Plano de Crescimento</p></b>'
                st.markdown(potencial, unsafe_allow_html=True)
            else:
                st.write("Médio Potencial de Desenvolvimento")
            st.metric("i3", f"{itres:.1f}%")
            if itres<10:
                potencial = '<b><p style="color:green">Alto Potencial de Desenvolvimento</p></b>'
                st.markdown(potencial, unsafe_allow_html=True)
            elif itres>15:
                potencial = '<b><p style="color:red">Alerta Plano de Crescimento</p></b>'
                st.markdown(potencial, unsafe_allow_html=True)
            else:
                st.write("Médio Potencial de Desenvolvimento")

    else:
        st.write('Clique no botão para calcular as métricas')