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
visible_phrases = 3  # Nombre de phrases visibles
scroll_height = len(phrases) * phrase_height

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
            height: {phrase_height * visible_phrases}px; /* Hauteur visible pour 3 phrases */
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
            transition: transform 0.5s ease-in-out;
        }}

        /* Styles des phrases */
        .phrase {{
            width: 100%;
            text-align: center;
            font-size: 16px;
            height: {phrase_height}px;
            line-height: {phrase_height}px;
            opacity: 0.6;
            transform: scale(0.8);
            transition: all 0.3s ease-in-out;
        }}

        /* Style pour la phrase centrale */
        .current {{
            font-size: 24px;
            font-weight: bold;
            opacity: 1;
            transform: scale(1);
        }}
    </style>

    <script>
        const scrollContent = document.getElementById("scroll-content");
        const phraseElements = document.querySelectorAll(".phrase");

        const totalPhrases = {len(phrases)};
        let currentIndex = 0;

        // Fonction pour mettre à jour les styles des phrases
        function updatePhrases() {{
            // Réinitialiser toutes les classes
            phraseElements.forEach(el => el.classList.remove("current"));

            // Déterminer l'index de la phrase centrale
            const centralIndex = currentIndex % totalPhrases;

            // Ajouter la classe 'current' uniquement à la phrase centrale
            if (phraseElements[centralIndex]) {{
                phraseElements[centralIndex].classList.add("current");
            }}
        }}

        // Fonction de défilement automatique
        function scroll() {{
            currentIndex += 1;
            if (currentIndex >= totalPhrases) {{
                currentIndex = 0; // Réinitialisation en boucle
                scrollContent.style.transition = 'none'; // Désactiver temporairement la transition
                scrollContent.style.transform = 'translateY(0px)'; // Réinitialisation instantanée
                void scrollContent.offsetWidth; // Forcer un reflow pour appliquer les changements
                scrollContent.style.transition = 'transform 0.5s ease-in-out'; // Réactiver la transition
            }}

            // Déplacer le contenu
            const translateY = -currentIndex * {phrase_height};
            scrollContent.style.transform = "translateY(" + translateY + "px)";

            // Mettre à jour les phrases
            updatePhrases();
        }}

        // Initialisation
        updatePhrases();
        setInterval(scroll, 3000); // Défilement toutes les 3 secondes
    </script>
"""

# Intégrer le contenu HTML/CSS/JS dans l'application Streamlit
components.html(html_content, height=300, width=600)
