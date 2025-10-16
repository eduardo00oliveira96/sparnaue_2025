import streamlit as st

st.set_page_config(page_title="Os Sparnauê", page_icon="🍻", layout="centered")

st.title("🌴🔥 OS SPARNAUÊ 🔥🌴")
st.image("assets/logo.png",width='stretch')

st.markdown(
    """
    ## “Tudo começou na Casa de Farinha…”

    Numa noite chuvosa, entre cachaça e risadas que batiam nas paredes,  
    nasceu o **clã dos Sparnauê**.  

    Entre goles de Fanta com vodka, churrasco e piadas de humor negro,  
    eles descobriram que o verdadeiro ritual da vida envolve:

    - Carne na brasa 🥩  
    - Copos levantados até o último gole 🥃  
    - Piadas que até o cão tem medo 😏  
    - Risadas que fazem os petistas tremerem 🐁  
    - Dança com a cachaça, o gelo e a música que ninguém lembra direito 🎶
"""
)

st.markdown(
    """
    ### 🌀 Evolução dos Locais Sagrados
    - **Casa de Farinha**: onde tudo começou, o solo coberto de lixo e a zoeira sem limites.  
    - **Geladão do Diabo Loiro**: o segundo templo, onde cerveja gelada escorria pelos dedos e as histórias de um salão que na verdade era um puteiro.  
    - **Pizzaria Estrela**: último reduto sagrado, onde o recheio ia de ponta a ponta e ninguém saía sem reclamar 🍕🔥  

    Aqui, os Sparnauê **não seguem regras**. Seguem o instinto, o prazer e a amizade que atravessa todas as noites.  
"""
)

st.markdown("---")

# --- Carrossel ---
# --- Carrossel ---
st.subheader("📸🎥 Momentos Épicos dos Sparnauê")

# Lista de arquivos (imagens e vídeos)
st.video("assets/sitio-1.mp4")
