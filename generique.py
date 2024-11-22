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
            height: 120px; /* Hauteur visible du conteneur (3 phrases * 40px) */
            overflow: hidden;
            background-color: #ffffff; /* Couleur de fond */
            display: flex;
            align-items: center;
            justify-content: center;
            border: none; /* Pas de bordure */
        }}
        #scroll-content {{
            display: flex;
            flex-direction: column;
            position: absolute;
            top: 0;
            left: 0;
            transition: transform 0.5s ease-in-out;
        }}
        .phrase {{
            width: 100%;
            text-align: center;
            font-size: 16px;
            height: 40px;
            line-height: 40px;
            box-sizing: border-box;
            opacity: 0.6;
            transition: all 0.5s ease-in-out;
        }}
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

        const totalPhrases = {len(phrases)};
        let currentIndex = 0;

        // Initialisation
        updatePhrases();

        // Fonction pour mettre à jour les classes
        function updatePhrases() {{
            // Réinitialiser toutes les classes
            phraseElements.forEach(el => el.classList.remove("current"));

            // Ajouter la classe 'current' à la phrase centrale
            if (phraseElements[currentIndex]) {{
                phraseElements[currentIndex].classList.add("current");
            }}

            // Calculer la nouvelle position
            const translateY = -currentIndex * 40; // 40px est la hauteur de chaque phrase
            scrollContent.style.transform = `translateY(${{translateY}}px)`;
        }}

        // Fonction pour passer à la phrase suivante
        function nextPhrase() {{
            currentIndex = (currentIndex + 1) % totalPhrases;
            updatePhrases();
        }}

        // Changer de phrase toutes les 3 secondes avec animation
        setInterval(nextPhrase, 3000); // Change phrase every 3 seconds
    </script>
"""

# Intégrer le contenu HTML/CSS/JS dans l'application Streamlit
components.html(html_content, height=220)
