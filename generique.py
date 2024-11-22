import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Défilement Continu", layout="centered")

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

# Générer le contenu HTML pour les phrases
phrases_html = "<br>".join(phrases * 3)  # Répéter les phrases pour une boucle infinie

# Ajouter le style CSS pour l'animation
st.markdown(f"""
    <style>
    .scroll-container {{
        position: relative;
        height: 200px;  /* Ajustez la hauteur selon vos besoins */
        overflow: hidden;
        border: 2px solid #f0f0f0;
        border-radius: 10px;
        background-color: #ffffff;
    }}
    .scroll-content {{
        display: inline-block;
        position: absolute;
        width: 100%;
        animation: scrollUp 20s linear infinite;
    }}
    .scroll-content p {{
        text-align: center;
        font-size: 18px;
        padding: 10px 0;
        margin: 0;
    }}
    @keyframes scrollUp {{
        0% {{
            top: 0;
        }}
        100% {{
            top: -{len(phrases) * 40}px; /* Ajustez le pixel en fonction de la hauteur des éléments */
        }}
    }}
    </style>
    
    <div class="scroll-container">
        <div class="scroll-content">
            <p>{phrases_html}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Optionnel : Ajouter un espace ou d'autres éléments de la page
st.write("Bienvenue sur la page de défilement continu des phrases !")
