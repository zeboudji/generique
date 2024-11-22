import streamlit as st

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

# Fonction pour afficher la phrase actuelle
def show_phrase():
    st.markdown(f"<h2 style='text-align: center;'>{phrases[st.session_state.index]}</h2>", unsafe_allow_html=True)

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

# Affichage de la phrase actuelle
show_phrase()

# Vérifier si on a atteint la fin ou le début pour inverser le sens
if st.session_state.forward and st.session_state.index == len(phrases) - 1:
    st.session_state.forward = False
elif not st.session_state.forward and st.session_state.index == 0:
    st.session_state.forward = True
