import streamlit as st
import time

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

# État initial
if 'index' not in st.session_state:
    st.session_state.index = 0
    st.session_state.forward = True

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
        st.markdown(f"<h2 style='text-align: center; animation: fadeIn 0.5s;'>{phrases[st.session_state.index]}</h2>", unsafe_allow_html=True)
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

# Gestion des événements du clavier
def key_event():
    key = st.session_state.key_pressed
    if key == "Left":
        if st.session_state.forward:
            st.session_state.index -= 1
            if st.session_state.index < 0:
                st.session_state.index = 0
        else:
            st.session_state.index += 1
            if st.session_state.index >= len(phrases):
                st.session_state.index = len(phrases) - 1
    elif key == "Right":
        if st.session_state.forward:
            st.session_state.index += 1
            if st.session_state.index >= len(phrases):
                st.session_state.index = len(phrases) - 1
        else:
            st.session_state.index -= 1
            if st.session_state.index < 0:
                st.session_state.index = 0
    st.session_state.key_pressed = ""  # Réinitialiser la touche
    st.experimental_rerun()

# Champ texte invisible pour capter les touches
st.text_input("", key="key_pressed", on_change=key_event)

# Cacher le champ texte
st.markdown("""
    <style>
    div[data-testid="stTextInput"] > div > input {
        position: absolute;
        opacity: 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Affichage des phrases avec animation
show_phrases()

# Vérifier si on a atteint la fin ou le début pour inverser le sens
if st.session_state.forward and st.session_state.index == len(phrases) - 1:
    st.session_state.forward = False
elif not st.session_state.forward and st.session_state.index == 0:
    st.session_state.forward = True
