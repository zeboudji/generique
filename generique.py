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
            margin: 0 auto;
            height: 120px; /* Hauteur visible du conteneur */
            overflow: hidden;
            background-color: #ffffff; /* Couleur de fond */
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        #scroll-content {{
            display: flex;
            flex-direction: column;
            animation: scroll 30s linear infinite;
        }}
        .phrase {{
            width: 100%;
            text-align: center;
            font-size: 16px;
            padding: 10px 0;
            box-sizing: border-box;
            opacity: 0.6;
            transition: transform 0.5s, opacity 0.5s;
        }}
        .current {{
            font-size: 24px;
            opacity: 1;
            transform: scale(1.2);
        }}
        @keyframes scroll {{
            0% {{
                transform: translateY(0);
            }}
            100% {{
                transform: translateY(-50%);
            }}
        }}
    </style>

    <script>
        const phrases = {phrases_js};
        const scrollContent = document.getElementById("scroll-content");
        const phraseElements = document.querySelectorAll(".phrase");

        // Calcul de la durée par phrase
        const animationDuration = 30; // Durée totale de l'animation en secondes
        const totalPhrases = {len(phrases)};
        const phraseDuration = animationDuration / totalPhrases;

        let currentIndex = 0;

        function updateCurrent() {{
            // Retirer la classe 'current' de toutes les phrases
            phraseElements.forEach(el => el.classList.remove("current"));

            // Ajouter la classe 'current' à la phrase actuelle
            if (currentIndex < phraseElements.length) {{
                phraseElements[currentIndex].classList.add("current");
            }}
        }}

        // Initialisation
        updateCurrent();

        // Mise à jour de la classe 'current' à chaque intervalle
        setInterval(() => {{
            currentIndex = (currentIndex + 1) % totalPhrases;
            updateCurrent();
        }}, phraseDuration * 1000);
    </script>
"""

# Intégrer le contenu HTML/CSS/JS dans l'application Streamlit
components.html(html_content, height=220)
