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

# Contenu HTML avec CSS et JavaScript intégrés
html_content = f"""
    <div id="scroll-container">
        <div id="scroll-content">
            {"".join([f'<div class="phrase">{phrase}</div>' for phrase in phrases])}
            <!-- Répéter les phrases pour une boucle infinie -->
            {"".join([f'<div class="phrase">{phrase}</div>' for phrase in phrases])}
        </div>
    </div>

    <style>
        #scroll-container {{
            position: relative;
            width: 80%;
            height: 100px; /* Hauteur visible du conteneur */
            margin: 0 auto;
            overflow: hidden;
            border: 2px solid #000; /* Optionnel : Bordure pour visualiser le conteneur */
            background-color: #f9f9f9; /* Optionnel : Couleur de fond */
        }}
        #scroll-content {{
            display: flex;
            flex-direction: column;
            animation: scroll 30s linear infinite;
        }}
        .phrase {{
            width: 100%;
            text-align: center;
            font-size: 24px;
            padding: 10px 0;
            box-sizing: border-box;
            opacity: 0;
            transform: translateY(20px);
            animation: fadeInOut 30s linear infinite;
        }}
        @keyframes scroll {{
            0% {{
                transform: translateY(0);
            }}
            100% {{
                transform: translateY(-50%);
            }}
        }}
        @keyframes fadeInOut {{
            0%, 100% {{ opacity: 0; }}
            5%, 25% {{ opacity: 1; }}
        }}
    </style>

    <script>
        // Ajuster la durée de l'animation en fonction du nombre de phrases
        const totalPhrases = {len(phrases)};
        const animationDuration = 30; // Durée totale de l'animation en secondes

        const scrollContent = document.getElementById("scroll-content");
        scrollContent.style.animation = `scroll ${animationDuration}s linear infinite`;

        const phrasesElements = document.querySelectorAll(".phrase");
        phrasesElements.forEach((el, index) => {{
            el.style.animation = `fadeInOut ${animationDuration}s linear infinite`;
            el.style.animationDelay = `${(index * animationDuration) / totalPhrases}s`;
        }});
    </script>
"""

# Intégrer le contenu HTML/CSS/JS dans l'application Streamlit
components.html(html_content, height=220)
