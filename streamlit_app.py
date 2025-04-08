import streamlit as st
import random
from PIL import Image
import requests
from io import BytesIO

# Konfiguracja strony
st.set_page_config(
    page_title="Jurassic ID",
    page_icon="🦖",
    layout="centered"
)

# Stylizacja z dodatkowym stylem dla ikony
st.markdown("""
<style>
    .main-header {font-size: 2.5rem; font-weight: bold; text-align: center;}
    .result-text {font-size: 1.5rem; font-weight: bold; margin-top: 1rem;}
    .centered-image {display: flex; justify-content: center;}
</style>
""", unsafe_allow_html=True)

# Ikona dinozaura - bardziej precyzyjne wyśrodkowanie
try:
    url = "https://img.icons8.com/?size=100&id=1cWHYsfc86W4&format=png&color=000000"
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    
    # Kontener z klasą CSS dla wyśrodkowania
    st.markdown('<div class="centered-image">', unsafe_allow_html=True)
    st.image(img, width=100, output_format="PNG")
    st.markdown('</div>', unsafe_allow_html=True)
except Exception:
    # Wyśrodkowany emoji dinozaura jako fallback
    st.markdown('<h1 style="text-align: center;">🦖</h1>', unsafe_allow_html=True)

# Tytuł aplikacji
st.markdown('<p class="main-header">Jurassic ID</p>', unsafe_allow_html=True)

# Dane dinozaurów
prefixes = [
    "Tyranno", "Stego", "Tricera", "Veloci", "Bronto", "Allo", "Ptero", "Ankylo", "Diplo", "Giganto",
    "Mega", "Micro", "Pachy", "Iguano", "Deinony", "Archaeo", "Apato", "Compso", "Ornitho", "Parasauro",
    "Austro", "Sino", "Dasplet", "Alber", "Carcharo", "Theriz", "Ovirap", "Hadro", "Argentin", "Bary"
]
suffixes = [
    "saurus", "raptor", "dactyl", "gnathus", "ceratops", "don", "mimus", "rex", "tops", "ptor",
    "venator", "long", "cyon", "pithecus", "cetus", "titan", "onychus", "odont", "opteryx", "rhinus",
    "pelta", "nyx", "draco", "suchus", "lophus", "therium", "oides", "ator", "osaurus", "odon"
]

# Pole do wprowadzania imienia
name = st.text_input("Wpisz swoje imię:")

# Funkcja generująca nazwę dinozaura
def create_dino_name(name):
    name = name.lower()
    if random.choice([True, False]):
        prefix = random.choice(prefixes)
        name_part = name[:-2] if len(name) > 3 else name
        suffix = name[-2:] if len(name) > 3 else ""
        return f"{prefix}{name_part}{suffix}"
    else:
        suffix = random.choice(suffixes)
        name_part = name[:3] if len(name) > 3 else name
        return f"{name_part.capitalize()}{suffix}"

# Przycisk do generowania nazwy
if st.button("Generuj nazwę dinozaura", type="primary"):
    if not name:
        st.error("Proszę wpisać imię!")
    else:
        dino_name = create_dino_name(name)
        st.markdown(f'<p class="result-text">Twój dinozaur: {dino_name}</p>', unsafe_allow_html=True)