import streamlit as st
import json
import streamlit.components.v1 as components

# Configuration de la page
st.set_page_config(page_title="Effet Texte Porsche", layout="centered")

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

# Sérialiser les phrases en format JSON pour JavaScript
phrases_js = json.dumps(phrases)

# Calculer la hauteur totale du scroll-content
phrase_height = 40  # Hauteur de chaque phrase en pixels
total_phrases = len(phrases)
scroll_height = total_phrases * phrase_height

# Contenu HTML avec CSS et JavaScript intégrés
html_content = f"""
    <div id="scroll-container">
        <div id="scroll-content">
            {"".join([f'<div class="phrase">{phrase}</div>' for phrase in phrases])}
            {"".join([f'<div class="phrase">{phrase}</div>' for phrase in phrases])} <!-- Duplication pour boucle infinie -->
        </div>
    </div>

    <style>
        /* Conteneur principal */
        #scroll-container {{
            position: relative;
            width: 80%;
            height: 120px; /* Hauteur visible du conteneur (3 phrases * 40px) */
            margin: 0 auto;
            overflow: hidden;
            background-color: #ffffff; /* Couleur de fond */
            border: none; /* Pas de bordure */
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            border-radius: 10px;
        }}

        /* Contenu défilant */
        #scroll-content {{
            display: flex;
            flex-direction: column;
            animation: scroll {total_phrases * 1.5}s linear infinite alternate;
        }}

        /* Styles des phrases */
        .phrase {{
            width: 100%;
            text-align: center;
            font-size: 16px;
            height: 40px;
            line-height: 40px;
            box-sizing: border-box;
            opacity: 0.6;
            transition: all 0.3s ease-in-out;
            position: relative;
        }}

        /* Mise en évidence de la phrase centrale */
        .phrase:nth-child(3), .phrase:nth-child({3 + total_phrases}) {{
            font-size: 24px;
            opacity: 1;
            color: #FF0000; /* Couleur de mise en évidence (Rouge Porsche) */
            font-weight: bold;
            transform: scale(1.2);
        }}

        /* Animation de défilement */
        @keyframes scroll {{
            0% {{
                transform: translateY(0);
            }}
            100% {{
                transform: translateY(-{total_phrases * phrase_height}px);
            }}
        }}
    </style>

    <script>
        // Ajuster la durée de l'animation en fonction du nombre de phrases
        const totalPhrases = {len(phrases)};
        const animationDuration = totalPhrases * 1.5; // 1.5 secondes par phrase
        document.getElementById('scroll-content').style.animationDuration = animationDuration + 's';
    </script>
"""

# Intégrer le contenu HTML/CSS/JS dans l'application Streamlit
components.html(html_content, height=160)
