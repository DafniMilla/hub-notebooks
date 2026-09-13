import streamlit as st


st.set_page_config(
    page_title="Hub de Notebooks",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)


NOTEBOOKS = {
    "2023": {
        "1º Semestre": "https://colab.research.google.com/drive/1xSli5rWGUhvqQzIR7IO4N-DkMnjPheNk",
        "2º Semestre": "https://colab.research.google.com/drive/1QOFPBFMueCgisVV8SSfm4JCHnwD_hjCS?usp=sharing",
    },
    "2022": {
        "1º Semestre": "https://colab.research.google.com/drive/1DNkytmjlS5_Whb7_2fhe1V7I3oSGn3ho",
        "2º Semestre": "https://colab.research.google.com/drive/1GLv7fVOd412gQV52leyGCrxS54p-5yqr",
    },
    "2021": {
        "1º Semestre": "https://colab.research.google.com/drive/1gHohNWpMy-gWdOW_Cms4Tdwi1ns3jwAf",
        "2º Semestre": "https://colab.research.google.com/drive/1EIInT_XSMgewGFYulF_s-ad8xhnjRFIC",
    },
    "2020": {
        "1º Semestre": "https://colab.research.google.com/drive/1TRHENoilA0jFH0gtjL2biH-v6h2N711p",
        "2º Semestre": "https://colab.research.google.com/drive/1PsqJk4D9IlfaRY6j2uKk9Ukzw2BtRTcz",
    },
    "2019": {
        "1º Semestre": "https://colab.research.google.com/drive/1n3kPG9hIF3j86U0H44e53mDDFWI1fIY-",
        "2º Semestre": "https://colab.research.google.com/drive/1gpwKCO19fORoCBTPuaSyuc8ROMfgrvnJ",
    },
    "2018": {
        "1º Semestre": "https://colab.research.google.com/drive/1HxnC162Ub722jdW3KwdW8YFk9uqza2Eb",
        "2º Semestre": "https://colab.research.google.com/drive/1XXj4L4zj5L43kcwxLUY7Vo1eqCqJYDHt",
    },
    "2017": {
        "1º Semestre": "https://colab.research.google.com/drive/1o-aH6C_nWXfrGEnYN33d0GaTZk2YbNAG",
        "2º Semestre": "https://colab.research.google.com/drive/1mVleiyEsF1bqN2Vcl5GC_XcQE88buB3Z",
    },
    "2016": {
        "1º Semestre": "https://colab.research.google.com/drive/1BkbV2mhHoWoXeDPpuNIRpTCCA2X-cqUj",
        "2º Semestre": "https://colab.research.google.com/drive/1ziGy9ZZEAnNZTEETuwoOwYGfHZMRv7i_",
    },
    "2015": {
        "1º Semestre": "https://colab.research.google.com/drive/1evazdkLk7rYkHTJsPBAOe6xONe-9UIQC",
        "2º Semestre": "https://colab.research.google.com/drive/11k39TLUg50K1lEQVd5ySVdfUdhN8A_pI",
    },
    "2014": {
        "1º Semestre": "https://colab.research.google.com/drive/1ynYZFvQi0ynq0hfyzHcedFlwvHn1ZqBm",
        "2º Semestre": "https://colab.research.google.com/drive/1Vjln4g3Bvx3BiAsi4iSk06FKkpLLT0lp",
    },
    "2013": {
        "1º Semestre": "https://colab.research.google.com/drive/1CxxnO7hU_bU_3siXmgcwz7DRlTzks_at",
        "2º Semestre": "https://colab.research.google.com/drive/1XdDENKkZ9Dd8TxbrgzArXGkoyCt9TMpa",
    },
    "2012": {
        "1º Semestre": "https://colab.research.google.com/drive/1VPWh1py7e0jwy3I_lh2FNGBE8-QatiuN",
        "2º Semestre": "https://colab.research.google.com/drive/1-VjmWb_mVzrtkn-1aAJIV9pNS2pvD9r-",
    },
    "2011": {
        "1º Semestre": "https://colab.research.google.com/drive/1OvqzbMreyeoWO10aOE-lnNP2zZ1Z-4Oh",
        "2º Semestre": "https://colab.research.google.com/drive/1UQVtnX58CLD0fTBPi0-rLvcKlcmKOlWy",
    },
}

st.markdown(
    """
    <style>
    @keyframes floatUpDown {
        0%   { transform: translateY(0px); }
        50%  { transform: translateY(-15px); }
        100% { transform: translateY(0px); }
    }
    @keyframes fadeInUp {
        0%   { opacity: 0; transform: translateY(30px); }
        100% { opacity: 1; transform: translateY(0px); }
    }
    @keyframes gradientShift {
        0%   { background-position: 0% 50%; }
        50%  { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .hero-container {
        text-align: center;
        padding: 50px 20px;
        border-radius: 20px;
        background: linear-gradient(-45deg, #1f4068, #162447, #1b1b2f, #0f3460);
        background-size: 400% 400%;
        animation: gradientShift 12s ease infinite;
        margin-bottom: 30px;
    }

    .hero-icon {
        font-size: 80px;
        animation: floatUpDown 3s ease-in-out infinite;
        display: inline-block;
    }

    .hero-title {
        color: white;
        font-size: 42px;
        font-weight: 800;
        margin-top: 10px;
        animation: fadeInUp 1s ease-out;
    }

    .hero-subtitle {
        color: #d0d7e5;
        font-size: 18px;
        margin-top: 10px;
        animation: fadeInUp 1.4s ease-out;
    }

    .info-card {
        background-color: #f5f7fa;
        border-left: 5px solid #1f4068;
        padding: 20px 25px;
        border-radius: 10px;
        margin-bottom: 15px;
        animation: fadeInUp 1.6s ease-out;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


st.sidebar.title("📂 Menu")
pagina = st.sidebar.radio("Navegação", ["🏠 Início"] + [f"📅 {ano}" for ano in NOTEBOOKS.keys()])



if pagina == "🏠 Início":
    st.markdown(
        """
        <div class="hero-container">
            <div class="hero-icon">📚</div>
            <div class="hero-title">Hub de Notebooks</div>
            <div class="hero-subtitle">Dados do Sisu (2011–2023)</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="info-card">
        <h4>👋 Bem-vindo!</h4>
        <p>
        Este painel reúne, em um só lugar, o acesso a todos os notebooks desenvolvidos,
        separados por ano e semestre. Use o menu à esquerda para
        selecionar o ano desejado e, em seguida, clique no botão do semestre para abrir
        o notebook correspondente diretamente no Google Colab.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Anos disponíveis", len(NOTEBOOKS))
    with col2:
        total_nb = sum(len(v) for v in NOTEBOOKS.values())
        st.metric("Notebooks", total_nb)
    with col3:
        st.metric("Fonte", "Google Colab")

    st.info("💡 Selecione um ano no menu lateral para ver os notebooks disponíveis.")


else:
    ano_selecionado = pagina.replace("📅 ", "")
    st.header(f"📅 Notebooks de {ano_selecionado}")
    st.write("Clique em um dos botões abaixo para abrir o notebook correspondente no Google Colab (nova aba).")
    st.write("")

    semestres = NOTEBOOKS[ano_selecionado]
    cols = st.columns(len(semestres))

    for col, (semestre, link) in zip(cols, semestres.items()):
        with col:
            st.subheader(semestre)
            if link == "COLE_O_LINK_AQUI":
                st.warning("Link ainda não configurado.")
                st.button(f"Abrir {semestre}", disabled=True, key=f"{ano_selecionado}_{semestre}_disabled")
            else:
                st.link_button(f"🚀 Abrir {semestre}", link, use_container_width=True)
