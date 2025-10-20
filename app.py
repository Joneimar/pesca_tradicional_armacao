import streamlit as st


st.set_page_config(
    page_title="Pesca Artesanal",
    page_icon="🎣",
    initial_sidebar_state="collapsed"
)

with open("styles/main.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.image('data/Logo_ic.png')

# Rodapé
st.markdown(
    """
    <div class="footer">
        <p>&copy; Este material é resultado do Curso de Formação de Agentes Patrimoniais e Ambientais edital 01/2025, realizado no âmbito do Programa de Visitação e Conservação da Ilha do Campeche.</p>
    </div>
    """, 
    unsafe_allow_html=True
)

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


