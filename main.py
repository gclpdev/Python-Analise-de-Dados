    ## Desenvolvedor Responsável pelo Projeto: Gabriel Oliveira
    ## Escopo do Projeto : Analisar Dados de uma Planilha com pandas, ydata_profilling & streamlit
    ## Data de Ínicio : Dom, 05 novembro de 2023


# Importando as Depêndencias necessárias:

import pandas as pd
from ydata_profiling import ProfileReport
import streamlit as st


# Logo após importaremos a Planilha em formato CSV
imp_data = pd.read_csv('casasparaalugar.csv')

# Visualizar Dados na Planilha selecionada:
print(imp_data)

# Gerando relatório com o ydata_profiling
profile = ProfileReport(imp_data, title='Dados Alugueis Capitais', html={'style':{'full_width': True}})

# Salvando o relatório em um arquivo HTML
arquivo_html = "relatorio_producao.html"
profile.to_file(arquivo_html)

# Aqui iremos renderizar o nosso Relatório em uma página web
st.title("Relatório de Casas para Alugar 2023")
with open(arquivo_html, "r") as file:
    st.write(file.read(), unsafe_allow_html=True)
