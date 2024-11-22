import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Effet Texte Inversé", layout="centered")

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

# Convertir la liste des phrases en format JavaScript
phrases_js = "[\"" + "\", \"".join(phrases) + "\"]"

# Intégrer le composant HTML avec JavaScript et CSS
st.markdown(f"""
    <div id="text-container">
        <div class="phrase previous">&nbsp;</div>
        <div class="phrase current"></div>
        <div class="phrase next">&nbsp;</div>
    </div>

    <style>
        #text-container {{
            position: relative;
            width: 80%;
            margin: 0 auto;
            height: 100px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }}
        .phrase {{
            position: absolute;
            width: 100%;
            text-align: center;
            opacity: 0;
            transition: opacity 0.5s ease-in-out, transform 0.5s ease-in-out;
        }}
        .current {{
            font-size: 24px;
            opacity: 1;
            transform: translateY(0);
        }}
        .previous, .next {{
            font-size: 16px;
            opacity: 0.6;
        }}
        .previous {{
            transform: translateY(-30px);
        }}
        .next {{
            transform: translateY(30px);
        }}
    </style>

    <script>
        const phrases = {phrases_js};
        let index = 0;
        let forward = true;
        const container = document.getElementById("text-container");
        const current = container.querySelector(".current");
        const previous = container.querySelector(".previous");
        const next = container.querySelector(".next");

        function updatePhrases() {{
            // Pré-animation: réduire l'opacité et déplacer légèrement les phrases
            current.style.opacity = 0;
            previous.style.opacity = 0;
            next.style.opacity = 0;
            previous.style.transform = "translateY(-20px)";
            next.style.transform = "translateY(20px)";
            
            setTimeout(() => {{
                // Mettre à jour le contenu
                current.textContent = phrases[index];
                if (index > 0) {{
                    previous.textContent = phrases[index - 1];
                }} else {{
                    previous.innerHTML = "&nbsp;";
                }}
                if (index < phrases.length - 1) {{
                    next.textContent = phrases[index + 1];
                }} else {{
                    next.innerHTML = "&nbsp;";
                }}

                // Ré-animer pour afficher les nouvelles phrases
                current.style.opacity = 1;
                previous.style.opacity = 0.6;
                next.style.opacity = 0.6;
                previous.style.transform = "translateY(-30px)";
                next.style.transform = "translateY(30px)";
            }}, 500); // Temps de la pré-animation
        }}

        function changePhrase() {{
            if (forward) {{
                if (index < phrases.length - 1) {{
                    index += 1;
                }} else {{
                    forward = false;
                    index -= 1;
                }}
            }} else {{
                if (index > 0) {{
                    index -= 1;
                }} else {{
                    forward = true;
                    index += 1;
                }}
            }}
            updatePhrases();
        }}

        // Initial display
        updatePhrases();

        // Rafraîchir toutes les 2 secondes
        setInterval(changePhrase, 2000);
    </script>
    """, unsafe_allow_html=True)
