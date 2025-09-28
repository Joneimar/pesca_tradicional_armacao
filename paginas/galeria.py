import streamlit as st
import os
from PIL import Image, ExifTags
import re


# Função para corrigir orientação da imagem
def abrir_imagem_com_rotacao(caminho):
    img = Image.open(caminho)
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break
        exif = dict(img._getexif().items())
        if exif.get(orientation) == 3:
            img = img.rotate(180, expand=True)
        elif exif.get(orientation) == 6:
            img = img.rotate(270, expand=True)
        elif exif.get(orientation) == 8:
            img = img.rotate(90, expand=True)
    except (AttributeError, KeyError, IndexError, TypeError):
        # imagem não tem EXIF
        pass
    return img

# Função para listar imagens ordenadas
def listar_imagens(caminho, max_imagens=9):
    imagens = [img for img in os.listdir(caminho) if img.lower().endswith((".png", ".jpg", ".jpeg"))]
    
    def extrair_numero(nome):
        match = re.search(r'IMG_(\d+)', nome, re.IGNORECASE)
        return int(match.group(1)) if match else 0

    imagens.sort(key=extrair_numero)
    return [os.path.join(caminho, img) for img in imagens[:max_imagens]]

# Mostrar galeria com correção de rotação
def mostrar_galeria(caminho, titulo, caption, link_drive):
    imagens = listar_imagens(caminho)
    
    with st.container(border=True):
        st.header(titulo, anchor=False)
        st.caption(caption)
        
        for i in range(0, len(imagens), 3):
            cols = st.columns(3)
            for j, img_path in enumerate(imagens[i:i+3]):
                img = abrir_imagem_com_rotacao(img_path)  # Corrige rotação
                cols[j].image(img, use_container_width=True)
        
        st.markdown(f"[Ver todas as fotos no Drive]({link_drive})", unsafe_allow_html=True)

# Página de Galeria
def galeria_page():
    st.title("Galeria de Fotos")
    st.write("Aqui você encontrará uma coleção de fotos relacionadas à pesca artesanal na Armação do Pântano do Sul - SC.")

    mostrar_galeria(
        "data/fotos/PESCA DA TAINHA 2024/",
        "Pesca da Tainha 2024",
        "Fotos capturadas durante a temporada de pesca da tainha em 2024.",
        "https://photos.app.goo.gl/eiFK5UqewJEwFtr57"
    )

    mostrar_galeria(
        "data/fotos/APAAPS/",
        "APAAPS",
        "Fotos capturadas da Associação de Pescadores Artesanais da Armação do Pântano do Sul.",
        "https://photos.app.goo.gl/tqn1yPqomtMbGnsb8"
    )

if __name__ == "__main__":
    galeria_page()
