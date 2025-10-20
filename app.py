import streamlit as st


st.set_page_config(
    page_title="Pesca Artesanal",
    page_icon="🎣",
    initial_sidebar_state="collapsed"
)

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}  /* Esconde menu dos três pontinhos */
    
    /* Estilo do rodapé customizado */
    .footer {
        background-color: #2c3e50 !important;
        color: white !important;
        padding: 1rem !important;
        text-align: center !important;
        font-size: 0.9rem !important;
        border-top: 2px solid #eaab61 !important;
        margin-top: 2rem !important;
        border-radius: 5px 5px 0 0 !important;
    }

    /* Header */
    header {
        background-color: #eaab61 !important;
        height: 3rem;  /* altura fixa */
        display: flex;
        align-items: center;
        justify-content: center;
    }

    /* Conteúdo do header */
    header:before {
        content: "Repositório Multimídia";
        font-size: 18px;
        font-weight: bold;
        color: white;
        white-space: nowrap;   /* impede quebra de linha */
        padding-left: 3rem;       /* adiciona espaço lateral */
        display: inline-block; /* garante aplicação do padding */
    }
    /* Title principal */
    h1 {
        color: #66a088 !important;
    }

    /* Subheader */
    h2, h3 {
        color: #eaab61 !important;
    }

    /* Texto padrão */
    p {
        color: white !important;
        font-size: 1rem; /* equivalente ao h5 */
    }

    /* Fundo */
    .stApp {
        background-image: url("PESCA DA TAINHA 2024/IMG_2813.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.image('data/Logo_ic.png')

pages = st.tabs(['Home', 'Conteúdos Didáticos', 'Entrevistas', 'Galeria'])

with pages[0]:
    from paginas.home import *
    home_page()

with pages[1]:
    from paginas.conteudos_didaticos import *
    conteudos_didaticos_page()

with pages[2]:
    from paginas.entrevistas import *
    entrevistas_page()

with pages[3]:
    from paginas.galeria import *
    galeria_page()

# Rodapé customizado
st.markdown(
    """
    <div class="footer">
        <p>&copy; Este material é resultado do Curso de Formação de Agentes Patrimoniais e Ambientais edital 01/2025, realizado no âmbito do Programa de Visitação e Conservação da Ilha do Campeche.</p>
    </div>
    """, 
    unsafe_allow_html=True
)

