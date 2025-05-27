import streamlit as st
import pandas as pd

# Título
st.title("Tabela NRC 2001")

# Caminho local do arquivo Excel
arquivo_excel = "Ingredientes_NRC2001.xlsx"

# Carregamento do DataFrame
try:
    df = pd.read_excel(arquivo_excel)
    st.success("Arquivo carregado com sucesso!")

    # Verifica se a coluna de nome do ingrediente existe
    col_nome = None
    for col in df.columns:
        if "nome" in col.lower() and "ingrediente" in col.lower():
            col_nome = col
            break

    if col_nome:
        # Sidebar com filtro por ingrediente
        st.sidebar.header("Filtro por Ingrediente")
        ingredientes = df[col_nome].dropna().unique()
        ingrediente_selecionado = st.sidebar.selectbox(
            "Selecione um ingrediente", 
            options=["Todos"] + sorted(ingredientes.tolist())
        )

        # Aplicar filtro
        if ingrediente_selecionado != "Todos":
            df_filtrado = df[df[col_nome] == ingrediente_selecionado]
        else:
            df_filtrado = df

        # Exibir DataFrame
        st.dataframe(df_filtrado, use_container_width=True)
    else:
        st.warning("Coluna com nome do ingrediente não encontrada.")
except FileNotFoundError:
    st.error(f"O arquivo '{arquivo_excel}' não foi encontrado no diretório.")
except Exception as e:
    st.error(f"Ocorreu um erro ao carregar os dados: {e}")