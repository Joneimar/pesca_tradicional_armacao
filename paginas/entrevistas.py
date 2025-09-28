import streamlit as st

def entrevistas_page():
    st.title("Entrevistas com Pescadores")
    st.write("Aqui você encontrará entrevistas sobre a pesca artesanal na Armação do Pântano do Sul - SC.")

    with st.container(border=True):
        st.header("O Mar, a Casa e a Identidade (O Lugar Vivido)", anchor=False)
        st.audio(data="data/entrevistas/Rodrigo-P2.mp3", format="audio/mp3")
        st.audio(data="data/entrevistas/Josi-P3.mp3", format="audio/mp3")
        st.audio(data="data/entrevistas/Joca P4.mp3", format="audio/mp3")
        st.caption("Entrevista com Pescadores APPAS (Associação de Pescadores Artesanais da Armação do Pântano do Sul) (2025).")

    with st.container(border=True):
        st.header("O Segredo do Saber-Fazer (Conhecimento e Território)", anchor=False)
        st.audio(data="data/entrevistas/Rodrigo-P5.mp3", format="audio/mp3")
        st.audio(data="data/entrevistas/Josi-P6.mp3", format="audio/mp3")
        st.audio(data="data/entrevistas/Joca P7.mp3", format="audio/mp3")
        st.caption("Entrevista com Pescadores APPAS (Associação de Pescadores Artesanais da Armação do Pântano do Sul) (2025).")

    with st.container(border=True):
        st.header("A Luta e a Transformação (Conflitos e Pressões)", anchor=False)
        st.audio(data="data/entrevistas/Josi-P8.mp3", format="audio/mp3")
        st.audio(data="data/entrevistas/Rodrigo-P9.mp3", format="audio/mp3")
        st.caption("Entrevista com Pescadores APPAS (Associação de Pescadores Artesanais da Armação do Pântano do Sul) (2025).")

    with st.container(border=True):
        st.header("Legado e o Futuro da Armação (Cultura e Geração)", anchor=False)
        st.audio(data="data/entrevistas/Josi-P10.mp3", format="audio/mp3")
        st.audio(data="data/entrevistas/Joca P12.mp3", format="audio/mp3")
        st.caption("Entrevista com Pescadores APPAS (Associação de Pescadores Artesanais da Armação do Pântano do Sul) (2025).")

    with st.container(border=True):
        st.header("A Pesca e o Turismo à Ilha do Campeche (A Integração com o Território)", anchor=False)
        st.audio(data="data/entrevistas/Joca P14.mp3", format="audio/mp3")
        st.audio(data="data/entrevistas/Rodrigo-P15.mp3", format="audio/mp3")
        st.caption("Entrevista com Pescadores APPAS (Associação de Pescadores Artesanais da Armação do Pântano do Sul) (2025).")

