import streamlit as st
from streamlit_autorefresh import st_autorefresh  # Assurez-vous d'ajouter cette bibliothèque
import time

# Installation de la bibliothèque streamlit_autorefresh
# Vous devez ajouter 'streamlit-autorefresh' à votre fichier requirements.txt
# Requirements.txt:
# streamlit
# streamlit-autorefresh

# Configuration de la page
st.set_page_config(page_title="Effet Texte Inversé", layout="centered")

# Liste de vos phrases
phrases = [
    "La nouvelle offre d’acculturation à l’IA d’Inside est lancée.",
    "Après 10 ans d’expertise dans la transformation digitale.",
    "Après une année d'exploration de l'IA avec les meilleurs experts.",
    "La passion peut s’essouffler.",
    "Il serait fou de penser que",
    "Nous pouvons encore surprendre.",
    "Comme vous l’imaginez,",
    "L’enthousiasme finit toujours par s’éteindre.",
    "Il faut arrêter de dire que",
    "L’IA va transformer nos vies.",
    "Certains pensent même que",
    "L’IA est loin d'être une révolution.",
    "Il est donc difficile de croire que",
    "Cette offre est exceptionnelle et une avancée majeure.",
    "---",
    "Pourtant..."
]

# Initialisation complète de st.session_state
if 'index' not in st.session_state:
    st.session_state.index = 0
if 'forward' not in st.session_state:
    st.session_state.forward = True

# Utilisation de st_autorefresh pour rafraîchir l'application toutes les 3 secondes
count = st_autorefresh(interval=3 * 1000, key="auto_refresh")

# Fonction pour afficher les phrases avec le formatage
def show_phrases():
    # Conteneur pour l'animation
    container = st.empty()
    with container.container():
        # Phrase précédente
        if st.session_state.index > 0:
            st.markdown(f"<p style='text-align: center; font-size:16px; opacity:0.6;'>{phrases[st.session_state.index - 1]}</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p style='text-align: center; font-size:16px; opacity:0.6;'>&nbsp;</p>", unsafe_allow_html=True)
        
        # Phrase actuelle
        st.markdown(f"<h2 style='text-align: center; animation: fadeIn 1s;'>{phrases[st.session_state.index]}</h2>", unsafe_allow_html=True)
        
        # Phrase suivante
        if st.session_state.index < len(phrases) - 1:
            st.markdown(f"<p style='text-align: center; font-size:16px; opacity:0.6;'>{phrases[st.session_state.index + 1]}</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p style='text-align: center; font-size:16px; opacity:0.6;'>&nbsp;</p>", unsafe_allow_html=True)
        
        # Style pour l'animation
        st.markdown("""
            <style>
            @keyframes fadeIn {
                from {opacity: 0;}
                to {opacity: 1;}
            }
            </style>
            """, unsafe_allow_html=True)

# Fonction pour mettre à jour l'index
def update_index():
    if st.session_state.forward:
        st.session_state.index += 1
        if st.session_state.index >= len(phrases):
            st.session_state.index = len(phrases) - 1
            st.session_state.forward = False
    else:
        st.session_state.index -= 1
        if st.session_state.index < 0:
            st.session_state.index = 0
            st.session_state.forward = True

# Mettre à jour l'index à chaque rafraîchissement
update_index()

# Afficher les phrases avec animation
show_phrases()
