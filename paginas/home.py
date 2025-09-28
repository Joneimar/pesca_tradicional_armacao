import streamlit as st

def home_page():
    with st.container(horizontal_alignment='center'):
        st.markdown("<h1 style='text-align: center; color: #66a088;'>Pesca Artesanal na Armação do Pântano do Sul - SC</h1>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center; color: gray;'>Repositório Piloto de Saberes e Práticas Tradicionais</h5>", unsafe_allow_html=True)

    st.divider()

    st.image('data/fotos/IMG_2804.jpg', caption='Pesca da Tainha na Armação do Pântano do Sul - SC (2024)', use_container_width=True)

    st.markdown(
        """
        <p style='text-align: justify;'>
        A pesca artesanal é uma prática <span style="color:#66a088; font-weight:bold;">tradicional</span> que marca profundamente a <span style="color:#EAAB61; font-style:italic;">identidade cultural</span> da Armação do Pântano do Sul, em Florianópolis (SC). Por gerações, os pescadores locais têm utilizado técnicas transmitidas oralmente, com <span style="color:#66a088; font-weight:bold;">embarcações simples</span>, <span style="color:#66a088; font-weight:bold;">redes</span> e outros <span style="color:#EAAB61; font-style:italic;">instrumentos manuais</span>, garantindo não apenas a subsistência de suas famílias, mas também a preservação de <span style="color:#66a088; font-weight:bold;">saberes e modos de vida ligados ao mar</span>.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style='text-align: justify;'>
        Essa comunidade também é uma das responsáveis pelo transporte de visitantes até o <span style="color:#66a088; font-weight:bold;">Patrimônio Arqueológico e Paisagístico Ilha do Campeche</span> 🏝️, integrando-se ao <span style="color:#EAAB61; font-style:italic;">turismo</span>, à <span style="color:#66a088; font-weight:bold;">memória</span> e à <span style="color:#EAAB61; font-style:italic;">sustentabilidade</span> do território.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style='text-align: justify;'>
        O <span style="color:#66a088; font-weight:bold;">Repositório Piloto</span> surge como uma iniciativa de <span style="color:#EAAB61; font-style:italic;">registro e valorização</span> dessa prática. Ele reúne:
        <ul>
            <li>📚 <span style="color:#66a088;">Materiais Didáticos</span></li>
            <li>🎤 <span style="color:#EAAB61;">Entrevistas</span></li>
            <li>🖼️ <span style="color:#66a088;">Galeria de Fotos</span></li>
            <li>📝 <span style="color:#EAAB61;">Materiais de Apoio</span></li>
        </ul>
        Tudo isso traduz a complexidade da pesca artesanal em linguagem acessível, possibilitando que <span style="color:#66a088; font-weight:bold;">conhecimentos acadêmicos</span> e <span style="color:#EAAB61; font-weight:bold;">experiências locais</span> se encontrem. Seu objetivo é ampliar o acesso à informação, tornando-a compreensível para diferentes públicos, desde pesquisadores até a própria comunidade e crianças que vivenciam esse ambiente.
        </p>
        """,
        unsafe_allow_html=True
    )