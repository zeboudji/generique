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
pourtant_index = phrases.index("Pourtant...")

# Créer une nouvelle liste de phrases à partir de "Pourtant..."
phrases_scrolling = phrases[pourtant_index+1:] + phrases[:pourtant_index+1]

# Sérialiser les phrases pour le JavaScript
phrases_js = json.dumps(phrases_scrolling)

# Calcul des dimensions
phrase_height = 50  # Hauteur de chaque phrase en pixels
visible_phrases = 3  # Nombre de phrases visibles (doit être impair pour avoir une phrase centrale)
scroll_duration = 30  # Durée totale du défilement (en secondes)

# HTML avec CSS et JavaScript
html_content = f"""
    <div id="scroll-container">
        <div id="scroll-content">
            {"".join([f'<div class="phrase">{phrase}</div>' for phrase in phrases_scrolling])}
            {"".join([f'<div class="phrase">{phrase}</div>' for phrase in phrases_scrolling])} <!-- Duplication pour boucle infinie -->
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
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        /* Contenu défilant */
        #scroll-content {{
            display: flex;
            flex-direction: column;
            position: relative;
            will-change: transform;
        }}

        /* Styles des phrases */
        .phrase {{
            width: 100%;
            text-align: center;
            font-size: 16px;
            height: {phrase_height}px;
            line-height: {phrase_height}px;
            opacity: 0.5;
            transform: scale(0.9);
            transition: all 0.5s ease-in-out;
        }}

        /* Style pour la phrase centrale */
        .current {{
            font-size: 24px;
            font-weight: bold;
            opacity: 1;
            transform: scale(1.1);
        }}
    </style>

    <script>
        const scrollContent = document.getElementById("scroll-content");
        const phraseElements = document.querySelectorAll(".phrase");
        const totalPhrases = {len(phrases_scrolling)};
        const phraseHeight = {phrase_height};
        let offset = 0;

        // Fonction pour mettre à jour les styles dynamiques
        function updateStyles() {{
            phraseElements.forEach((el, index) => {{
                el.classList.remove("current");
            }});

            const centerIndex = (offset + Math.floor({visible_phrases} / 2)) % totalPhrases;
            phraseElements[centerIndex].classList.add("current");
        }}

        // Fonction de défilement automatique
        function scroll() {{
            offset++;
            const translateY = -offset * phraseHeight;

            scrollContent.style.transition = "transform 0.5s ease-in-out";
            scrollContent.style.transform = "translateY(" + translateY + "px)";

            // Réinitialisation pour un défilement fluide
            if (offset >= totalPhrases) {{
                setTimeout(() => {{
                    scrollContent.style.transition = "none";
                    scrollContent.style.transform = "translateY(0px)";
                    offset = 0;
                    updateStyles();
                }}, 500); // Attendre la fin de la transition avant de réinitialiser
            }}

            updateStyles();
        }}

        // Démarrer l'animation
        setInterval(scroll, 2000); // Défilement toutes les 2 secondes
        updateStyles(); // Initialisation des styles
    </script>
"""

# Intégrer le HTML dans Streamlit
components.html(html_content, height=phrase_height * visible_phrases, width=700)
