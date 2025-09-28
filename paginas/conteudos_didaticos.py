import streamlit as st

def conteudos_didaticos_page():
    st.title("Conteúdos Didáticos")
    st.write("Aqui você encontrará materiais didáticos relacionados à pesca artesanal na Armação do Pântano do Sul - SC.")

    with st.container(border=True):   
        st.header("Vídeo didático: Mapeando a Mente do Mar", anchor=False)
        st.video("data/videos/Mapeando_a_Mente_do_Mar.mp4")
        # st.video("https://youtu.be/8l9O-S9DWUI")
        st.caption("Criado com Inteligência Artificial de escopo controlado (Notebook LM) a partir da dissertação de mestrado abaixo.")
        st.markdown(f"[O MUNDO É O MAR: PESCADORES TRADICIONAIS E SEUS MAPAS MENTAIS]({'https://drive.google.com/file/d/1Hk9I9GA7uTf-ETG-vBLZP2jB85t-aVLE/view?usp=sharing'})", unsafe_allow_html=True)

    with st.container(border=True):   
        st.header("Podcast: O Mar é Nossa Casa", anchor=False)
        st.audio(data="data/podcasts/O_Mar_é_Nossa_Casa.mp3", format="audio/mp3")
        st.caption("Criado com Inteligência Artificial de escopo controlado (Notebook LM) a partir da dissertação de mestrado abaixo.")
        st.markdown(f"[O MUNDO É O MAR: PESCADORES TRADICIONAIS E SEUS MAPAS MENTAIS]({'https://drive.google.com/file/d/1Hk9I9GA7uTf-ETG-vBLZP2jB85t-aVLE/view?usp=sharing'})", unsafe_allow_html=True)

    with st.container(border=True):   
        st.header("Folder: Pesca Artesanal", anchor=False)
        col1, col2 = st.columns(2)
        col1.image("data/folders/folder1_pag1.jpeg")
        col2.image("data/folders/folder1_pag2.jpeg")
        st.caption("Criado a partir de síntese histórica.")



