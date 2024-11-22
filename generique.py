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
        <div class="phrase previous">&nbsp;</div>
        <div class="phrase current"></div>
        <div class="phrase next">&nbsp;</div>
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
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }}
        .phrase {{
            width: 100%;
            text-align: center;
            font-size: 16px;
            opacity: 0.6;
            transition: all 0.5s ease-in-out;
            position: absolute;
            left: 0;
        }}
        .current {{
            font-size: 24px;
            opacity: 1;
            transform: translateY(0px) scale(1.2);
        }}
        .previous {{
            transform: translateY(-30px) scale(1);
        }}
        .next {{
            transform: translateY(30px) scale(1);
        }}
    </style>

    <script>
        const phrases = {phrases_js};
        let index = 0;
        const totalPhrases = phrases.length;

        const currentEl = document.querySelector('.current');
        let previousEl = document.querySelector('.previous');
        let nextEl = document.querySelector('.next');

        function updatePhrases() {{
            currentEl.textContent = phrases[index];
            previousEl.textContent = phrases[(index - 1 + totalPhrases) % totalPhrases];
            nextEl.textContent = phrases[(index + 1) % totalPhrases];
        }}

        function nextPhrase() {{
            // Retirer les classes actuelles
            currentEl.classList.remove('current');
            previousEl.classList.remove('previous');
            nextEl.classList.remove('next');

            // Ajouter les nouvelles classes
            currentEl.classList.add('previous');
            nextEl.classList.add('current');

            // Mettre à jour l'index
            index = (index + 1) % totalPhrases;

            // Mettre à jour les phrases
            updatePhrases();

            // Après la transition, réassigner les classes
            setTimeout(() => {{
                // Retirer les anciennes classes
                currentEl.classList.remove('previous');
                previousEl.classList.remove('previous');

                // Swap les éléments
                let temp = previousEl;
                previousEl = currentEl;
                currentEl = nextEl;
                nextEl = temp;

                // Mettre à jour la classe 'next' pour le nouvel élément suivant
                nextEl.classList.add('next');
            }}, 500); // Durée de la transition (0.5s)
        }}

        // Initialisation
        updatePhrases();

        // Changer de phrase toutes les 3 secondes avec animation
        setInterval(nextPhrase, 3000); // Change phrase every 3 seconds
    </script>
"""

# Intégrer le contenu HTML/CSS/JS dans l'application Streamlit
components.html(html_content, height=220)
