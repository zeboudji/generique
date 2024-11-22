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

# Sérialiser les phrases pour le JavaScript
phrases_js = json.dumps(phrases)

# Calcul des dimensions
phrase_height = 50  # Hauteur de chaque phrase en pixels
visible_phrases = 3  # Nombre de phrases visibles
scroll_duration = 10  # Durée totale du défilement (en secondes)

# HTML avec CSS et JavaScript
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
            animation: scroll {scroll_duration}s linear infinite;
        }}

        /* Styles des phrases */
        .phrase {{
            width: 100%;
            text-align: center;
            font-size: 14px;
            height: {phrase_height}px;
            line-height: {phrase_height}px;
            opacity: 0.3;
            transform: scale(0.8);
            transition: all 0.5s ease-in-out;
        }}

        /* Style pour la phrase centrale */
        .current {{
            font-size: 28px;
            font-weight: bold;
            opacity: 1;
            transform: scale(1.2);
        }}

        /* Keyframes pour le défilement fluide */
        @keyframes scroll {{
            0% {{ transform: translateY(0); }}
            100% {{ transform: translateY(-{len(phrases) * phrase_height}px); }}
        }}
    </style>

    <script>
        const scrollContent = document.getElementById("scroll-content");
        const phraseElements = document.querySelectorAll(".phrase");
        const totalPhrases = {len(phrases)};
        const phraseHeight = {phrase_height};
        let offset = 0;

        // Fonction pour mettre à jour les styles dynamiques
        function updateStyles() {{
            phraseElements.forEach((el, index) => {{
                el.classList.remove("current");

                // Calculer l'index de la phrase centrale visible
                const centerIndex = (offset + Math.floor({visible_phrases} / 2)) % totalPhrases;
                if (index === centerIndex) {{
                    el.classList.add("current");
                }}
            }});
        }}

        // Fonction de défilement automatique
        function scroll() {{
            offset++;
            const translateY = -offset * phraseHeight;

            // Réinitialisation pour un défilement fluide
            if (offset >= totalPhrases) {{
                offset = 0; // Réinitialiser à zéro
                scrollContent.style.transition = "none"; // Désactiver temporairement la transition
                scrollContent.style.transform = "translateY(0px)"; // Retour en haut
                void scrollContent.offsetWidth; // Forcer un reflow
                scrollContent.style.transition = "transform 0.5s ease-in-out"; // Réactiver la transition
            }} else {{
                scrollContent.style.transform = "translateY(" + translateY + "px)";
            }}

            updateStyles();
        }}

        // Démarrer l'animation
        setInterval(scroll, 1000); // Défilement toutes les secondes
        updateStyles(); // Initialisation des styles
    </script>
"""

# Intégrer le HTML dans Streamlit
components.html(html_content, height=300, width=600)
