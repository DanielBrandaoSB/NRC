import streamlit as st
import math
import pandas as pd

st.set_page_config(page_title="NRC 2001 - Nutrição de Vacas", layout="wide")

# Menu lateral com três páginas
pagina = st.sidebar.selectbox("Escolha a página", [
    "Requisitos Nutricionais",
    "Ingredientes - NRC 2001",
    "Ingredientes - Custo"
])

# Página 1: Requisitos Nutricionais
if pagina == "Requisitos Nutricionais":
    st.title("Requisitos Nutricionais - NRC 2001 (Lactação)")
    st.title("")
    
    st.sidebar.header("Dados do Animal")

    bw = st.sidebar.number_input("Peso corporal (kg)", min_value=300, max_value=1000, value=650)
    leite = st.sidebar.number_input("Produção de leite (kg/dia)", min_value=10.0, max_value=80.0, value=35.0)
    gordura = st.sidebar.number_input("Gordura do leite (%)", min_value=2.0, max_value=6.0, value=3.5)
    proteina = st.sidebar.number_input("Proteína do leite (%)", min_value=2.0, max_value=4.0, value=3.2)
    del_dias = st.sidebar.number_input("Dias em lactação (DEL)", min_value=1, max_value=400, value=130)

    wol = del_dias / 7
    fcm = 0.4 * leite + 15 * leite * (gordura / 100)
    dmi = (0.372 * fcm + 0.0968 * bw**0.75) * (1 - math.exp(-0.192 * (wol - 3.67)))

    nel_leite = 0.0929 * gordura + 0.0547 * proteina + 0.192
    nel_total = leite * nel_leite + 0.08 * bw**0.75

    y_prot = leite * (proteina / 100)
    mp_lact = (y_prot / 0.97) * 1000
    mp_manut = 3.8 * bw**0.75
    pb_total = (mp_lact + mp_manut) / (0.64 * 1000)
    mp_total = mp_lact + mp_manut

    fdn = 0.28 * dmi

    ca = (0.031 * bw + 1.2 * leite) / 1000
    p = (0.027 * bw + 0.9 * leite) / 1000
    mg = 0.0025 * dmi
    k = 0.012 * dmi
    na = 0.006 * dmi
    s = 0.0025 * dmi

    vit_a = 110 * bw
    vit_d = 30 * bw
    vit_e = 0.8 * dmi

    aa = {
        "Lisina": 0.072,
        "Metionina": 0.024,
        "Histidina": 0.022,
        "Treonina": 0.065,
        "Valina": 0.065,
        "Isoleucina": 0.062,
        "Leucina": 0.086,
        "Fenilalanina": 0.050,
        "Arginina": 0.048
    }
    aa_resultado = {k: round(v * mp_total, 1) for k, v in aa.items()}

    st.subheader("Resultados dos Requisitos Nutricionais")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### Matéria Seca e Energia")
        st.write(f"**DMI**: {dmi:.2f} kg/dia")
        st.write(f"**NEL total**: {nel_total:.2f} Mcal/dia")

    with col2:
        st.markdown("### Proteína e FDN")
        st.write(f"**PB total**: {pb_total:.2f} kg/dia")
        st.write(f"**FDN estimada**: {fdn:.2f} kg/dia")

    with col3:
        st.markdown("### Vitaminas (UI/dia)")
        st.write(f"Vitamina A: {vit_a:.0f}")
        st.write(f"Vitamina D: {vit_d:.0f}")
        st.write(f"Vitamina E: {vit_e:.0f}")

    st.markdown("---")
    st.markdown("### Minerais (kg/dia)")
    st.write(f"Cálcio: {ca:.3f}, Fósforo: {p:.3f}, Magnésio: {mg:.3f}, Potássio: {k:.3f}, Sódio: {na:.3f}, Enxofre: {s:.3f}")

    st.markdown("---")
    st.markdown("### Aminoácidos Essenciais (g/dia)")
    st.table(aa_resultado)

# Função compartilhada para leitura e filtro dos ingredientes
def processar_arquivo_com_filtro_individual(arquivo, titulo, chave_filtro):
    try:
        df = pd.read_excel(arquivo)
        col_nome = None
        for col in df.columns:
            if "ingrediente" in col.lower():
                col_nome = col
                break

        if col_nome:
            st.markdown(f"### {titulo}")
            ingredientes = df[col_nome].dropna().unique()
            ingrediente_selecionado = st.selectbox(
                f"🔎 Filtrar ingrediente - {titulo}",
                options=["Todos"] + sorted(ingredientes.tolist()),
                key=chave_filtro
            )

            if ingrediente_selecionado != "Todos":
                df_filtrado = df[df[col_nome] == ingrediente_selecionado]
            else:
                df_filtrado = df

            st.dataframe(df_filtrado, use_container_width=True)
        else:
            st.warning(f"⚠️ Coluna com nome do ingrediente não encontrada em {titulo}")
    except FileNotFoundError:
        st.error(f"❌ Arquivo '{arquivo}' não encontrado.")
    except Exception as e:
        st.error(f"❌ Erro ao processar '{titulo}': {e}")

# Página 2: Ingredientes - NRC 2001
if pagina == "Ingredientes - NRC 2001":
    st.title("Ingredientes - NRC 2001")
    processar_arquivo_com_filtro_individual("Ingredientes_NRC2001.xlsx", "Tabela NRC 2001", "filtro_nrc")

# Página 3: Ingredientes - Custo
if pagina == "Ingredientes - Custo":
    st.title("Ingredientes - Custo")
    processar_arquivo_com_filtro_individual("Ingredientes - Custo (2).xlsx", "Tabela de Custos", "filtro_custo")
