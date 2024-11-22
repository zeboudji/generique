import streamlit as st
import json
import streamlit.components.v1 as components

# Configuration de la page
st.set_page_config(page_title="Effet Texte Porsche", layout="centered")

# Liste des phrases
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

# Trouver l'index de "Pourtant..."
index_pourtant = phrases.index("Pourtant...") + 1  # +1 pour démarrer après "Pourtant..."

# Réorganiser la liste des phrases pour commencer à partir de "Pourtant..."
phrases_scrolling = phrases[index_pourtant:] + phrases[:index_pourtant]

# Calcul des dimensions
phrase_height = 50  # Hauteur de chaque phrase en pixels
visible_phrases = 3  # Nombre de phrases visibles (doit être impair pour une phrase centrale)
scroll_duration = 30  # Durée totale du défilement (en secondes)

# HTML avec CSS et JavaScript
html_content = f"""
    <div id="scroll-container">
        <div id="scroll-content">
            {''.join([f'<div class="phrase">{phrase}</div>' for phrase in phrases_scrolling])}
            {''.join([f'<div class="phrase">{phrase}</div>' for phrase in phrases_scrolling])} <!-- Duplication pour boucle infinie -->
        </div>
    </div>

    <style>
        /* Conteneur principal */
        #scroll-container {{
            position: relative;
            width: 80%;
            margin: 0 auto;
            height: {phrase_height * visible_phrases}px; /* Hauteur visible (3 phrases) */
            overflow: hidden;
        }}

        /* Contenu défilant */
        #scroll-content {{
            display: flex;
            flex-direction: column;
            animation: scroll {scroll_duration}s linear infinite;
        }}

        /* Styles des phrases */
        .phrase {{
            text-align: center;
            font-size: 14px;
            height: {phrase_height}px;
            line-height: {phrase_height}px;
            opacity: 0.5;
            transform: scale(0.9);
            transition: all 0.5s ease-in-out;
        }}

        /* Style pour la phrase centrale */
        .phrase:nth-child(3n + 2) {{
            font-size: 28px;
            font-weight: bold;
            opacity: 1;
            transform: scale(1.2);
        }}

        /* Keyframes pour le défilement fluide */
        @keyframes scroll {{
            0% {{ transform: translateY(0); }}
            100% {{ transform: translateY(-{len(phrases_scrolling) * phrase_height}px); }}
        }}
    </style>
"""

# Intégrer le HTML dans Streamlit
components.html(html_content, height=phrase_height * visible_phrases, width=700)
