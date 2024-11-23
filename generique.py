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
            margin: 0 auto;
            height: 120px; /* Hauteur visible du conteneur (3 phrases * 40px) */
            overflow: hidden;
            background-color: #ffffff; /* Couleur de fond */
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        /* Contenu défilant */
        #scroll-content {{
            display: flex;
            flex-direction: column;
            position: absolute;
            top: 0;
            left: 0;
            transform: translateY(0);
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
        }}

        /* Style de la phrase centrale */
        .current {{
            font-size: 24px;
            opacity: 1;
            transform: scale(1.2);
        }}
    </style>

    <script>
        const phrases = {phrases_js};
        const scrollContent = document.getElementById("scroll-content");
        const phraseElements = document.querySelectorAll(".phrase");

        const totalPhrases = {total_phrases};
        let position = 0;
        const phraseHeight = {phrase_height}; // Hauteur de chaque phrase en px
        const scrollSpeed = 0.5; // Vitesse de défilement (pixels par frame)
        const centralPosition = 60; // Position centrale en px (moitié de la hauteur du conteneur)

        // Fonction pour mettre à jour les classes des phrases
        function updatePhrases() {{
            // Réinitialiser toutes les classes
            phraseElements.forEach(el => el.classList.remove("current"));

            // Calculer l'indice de la phrase centrale
            const currentPhraseIndex = Math.floor((position + centralPosition - (phraseHeight / 2)) / phraseHeight);
            if (phraseElements[currentPhraseIndex]) {{
                phraseElements[currentPhraseIndex].classList.add("current");
            }}
        }}

        // Fonction de défilement
        function scroll() {{
            position -= scrollSpeed;
            scrollContent.style.transform = `translateY(${position}px)`;

            // Si le défilement a atteint la fin d'une boucle, réinitialiser la position
            if (position <= -{scroll_height}px) {{
                position += {scroll_height}px;
            }}

            updatePhrases();
            requestAnimationFrame(scroll);
        }}

        // Initialisation
        updatePhrases();
        scroll();
    </script>
"""

# Intégrer le contenu HTML/CSS/JS dans l'application Streamlit
components.html(html_content, height=220)
