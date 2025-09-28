import streamlit as st


st.set_page_config(
    page_title="Pesca Artesanal",
    page_icon="🎣",
    initial_sidebar_state="collapsed"
)

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}  /* Esconde menu dos três pontinhos */
    footer {visibility: hidden;}     /* Esconde rodapé */

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
        content: "Pesca Artesanal na Armação do Pântano do Sul";
        font-size: 18px;
        font-weight: bold;
        color: white;
        white-space: nowrap;   /* impede quebra de linha */
        padding: 0 1rem;       /* adiciona espaço lateral */
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

    
