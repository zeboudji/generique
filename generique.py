import streamlit as st
import streamlit.components.v1 as components

# Configuration de la page Streamlit
st.set_page_config(
    page_title="Publicité Porsche - Animation Texte",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Titre de l'application
st.title("Publicité Porsche - Animation Texte")

# HTML, CSS et JavaScript intégrés dans une chaîne multi-lignes
html_code = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Publicité Porsche - Animation Texte</title>
    <style>
        /* Styles de base pour le corps de la page */
        body {
            margin: 0;
            padding: 0;
            background-color: #000; /* Fond noir pour contraste */
            display: flex;
            justify-content: center; /* Centre horizontalement le conteneur */
            align-items: center; /* Centre verticalement le conteneur */
            height: 100vh; /* Hauteur de la fenêtre */
            overflow: hidden; /* Empêche le défilement de la page */
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; /* Police élégante */
        }

        /* Conteneur principal agrandi en largeur */
        #scroll-container {
            position: relative;
            width: 90%; /* Largeur ajustée à 90% de la fenêtre */
            max-width: 1600px; /* Largeur maximale augmentée pour éviter le rognage */
            height: 120px; /* Hauteur initiale (3 phrases * 40px) */
            overflow: hidden; /* Masque le contenu débordant */
            background-color: #000; /* Fond noir */
            border-radius: 10px; /* Coins arrondis */
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.7); /* Ombre portée pour profondeur */
            display: flex;
            justify-content: center; /* Centre le contenu horizontalement */
            align-items: center; /* Centre le contenu verticalement */
        }

        /* Contenu défilant */
        #scroll-content {
            display: flex;
            flex-direction: column; /* Arrange les phrases en colonne */
            position: absolute; /* Positionnement absolu pour permettre l'animation */
            top: 0;
            left: 0;
            animation: scroll 30s linear infinite alternate; /* Animation de défilement */
        }

        /* Styles des phrases */
        .phrase {
            width: 100%;
            text-align: center; /* Centre le texte horizontalement */
            font-size: 16px; /* Taille de police initiale */
            height: 40px;
            line-height: 40px; /* Aligne verticalement le texte */
            box-sizing: border-box;
            opacity: 0.6; /* Opacité réduite pour les phrases non centrales */
            transition: all 0.3s ease-in-out; /* Transition fluide pour les changements */
            color: #ffffff; /* Couleur du texte blanc */
            white-space: normal; /* Permet le retour à la ligne */
            word-wrap: break-word; /* Permet de casser les mots pour éviter le dépassement */
            overflow: hidden; /* Masque tout débordement */
        }

        /* Mise en évidence de la phrase centrale */
        .highlight {
            font-size: 24px; /* Taille de police augmentée pour la mise en évidence */
            opacity: 1; /* Opacité maximale */
            color: #E10600; /* Rouge Porsche */
            font-weight: bold; /* Texte en gras */
            transform: scale(1.2); /* Agrandissement de la phrase */
            text-shadow: 0 0 10px #E10600, 0 0 20px #E10600; /* Effet de lueur rouge */
        }

        /* Animation de défilement */
        @keyframes scroll {
            0% {
                transform: translateY(0);
            }
            100% {
                transform: translateY(-50%);
            }
        }

        /* Media Queries pour Responsivité */
        @media (max-width: 1600px) {
            #scroll-container {
                width: 95%; /* Ajuste la largeur à 95% pour les écrans plus petits */
                max-width: 1400px; /* Réduit la largeur maximale */
            }

            .phrase {
                font-size: 18px; /* Augmente légèrement la taille de la police */
            }

            .highlight {
                font-size: 24px; /* Taille de police pour la mise en évidence */
            }
        }

        @media (max-width: 1200px) {
            #scroll-container {
                width: 100%; /* Prend toute la largeur disponible */
                max-width: 1200px; /* Réduit la largeur maximale */
                height: 120px; /* Maintient la hauteur initiale */
            }

            .phrase {
                font-size: 16px; /* Taille de police réduite pour les petits écrans */
            }

            .highlight {
                font-size: 22px; /* Taille de police réduite pour la mise en évidence */
            }
        }
    </style>
</head>
<body>
    <div id="scroll-container">
        <div id="scroll-content">
            <!-- Phrases originales -->
            <div class="phrase">La nouvelle offre d’acculturation à l’IA d’Inside est lancée.</div>
            <div class="phrase">Après 10 ans d’expertise dans la transformation digitale.</div>
            <div class="phrase">Après une année d'exploration de l'IA avec les meilleurs experts.</div>
            <div class="phrase">La passion peut s’essouffler.</div>
            <div class="phrase">Il serait fou de penser que</div>
            <div class="phrase">Nous pouvons encore surprendre.</div>
            <div class="phrase">Comme vous l’imaginez,</div>
            <div class="phrase">L’enthousiasme finit toujours par s’éteindre.</div>
            <div class="phrase">Il faut arrêter de dire que</div>
            <div class="phrase">L’IA va transformer nos vies.</div>
            <div class="phrase">Certains pensent même que</div>
            <div class="phrase">L’IA est loin d'être une révolution.</div>
            <div class="phrase">Il est donc difficile de croire que</div>
            <div class="phrase">Cette offre est vraiment exceptionnelle !</div>
            <div class="phrase">---</div>
            <div class="phrase">Pourtant...</div>
            <!-- Phrases dupliquées pour boucle infinie -->
            <div class="phrase">La nouvelle offre d’acculturation à l’IA d’Inside est lancée.</div>
            <div class="phrase">Après 10 ans d’expertise dans la transformation digitale.</div>
            <div class="phrase">Après une année d'exploration de l'IA avec les meilleurs experts.</div>
            <div class="phrase">La passion peut s’essouffler.</div>
            <div class="phrase">Il serait fou de penser que</div>
            <div class="phrase">Nous pouvons encore surprendre.</div>
            <div class="phrase">Comme vous l’imaginez,</div>
            <div class="phrase">L’enthousiasme finit toujours par s’éteindre.</div>
            <div class="phrase">Il faut arrêter de dire que</div>
            <div class="phrase">L’IA va transformer nos vies.</div>
            <div class="phrase">Certains pensent même que</div>
            <div class="phrase">L’IA est loin d'être une révolution.</div>
            <div class="phrase">Il est donc difficile de croire que</div>
            <div class="phrase">Cette offre est vraiment exceptionnelle !</div>
            <div class="phrase">---</div>
            <div class="phrase">Pourtant...</div>
        </div>
    </div>

    <script>
        // Sélectionne le contenu défilant et toutes les phrases
        const scrollContent = document.getElementById('scroll-content');
        const phrases = document.querySelectorAll('.phrase');
        const container = document.getElementById('scroll-container');

        /**
         * Fonction pour mettre en évidence la phrase centrale
         * Parcourt toutes les phrases et applique la classe 'highlight' à celle qui est au centre du conteneur
         */
        function highlightCentralPhrase() {
            phrases.forEach(phrase => {
                // Récupère la position de la phrase et du conteneur
                const rect = phrase.getBoundingClientRect();
                const containerRect = container.getBoundingClientRect();

                // Calcule le centre de la phrase et le centre du conteneur
                const phraseCenterY = rect.top + rect.height / 2;
                const containerCenterY = containerRect.top + containerRect.height / 2;

                // Si le centre de la phrase est proche du centre du conteneur (tolérance de 20px)
                if (Math.abs(phraseCenterY - containerCenterY) < 20) {
                    phrase.classList.add('highlight'); // Ajoute la classe 'highlight'
                } else {
                    phrase.classList.remove('highlight'); // Retire la classe 'highlight'
                }
            });
        }

        /**
         * Fonction d'animation qui appelle highlightCentralPhrase à chaque frame
         */
        function animate() {
            highlightCentralPhrase();
            requestAnimationFrame(animate); // Appelle la fonction à la prochaine frame
        }

        // Démarre l'animation au chargement de la page
        window.addEventListener('load', () => {
            animate();
        });

        // Recalcule la mise en évidence lors du redimensionnement de la fenêtre
        window.addEventListener('resize', () => {
            highlightCentralPhrase();
        });
    </script>
</body>
</html>
"""

# Intégrer le contenu HTML/CSS/JS dans l'application Streamlit
# Utilisation de components.html pour afficher le HTML personnalisé
# Le paramètre height est ajusté en fonction de la hauteur du conteneur
components.html(html_code, height=200)  # Augmente légèrement la hauteur pour éviter les débordements

# Explications supplémentaires (facultatif)
st.markdown("""
---
**Remarque** :
- Assurez-vous que les phrases dans le HTML ne dépassent pas la largeur maximale du conteneur pour éviter tout rognage.
- Vous pouvez ajuster la largeur maximale (`max-width`) dans le CSS selon vos besoins.
- Pour une meilleure expérience visuelle, il est recommandé de visualiser l'application en plein écran.

**Déploiement** :
1. **Pousser le Code sur GitHub** :
   - Initialisez votre dépôt GitHub et poussez le fichier `app.py` avec le code ci-dessus.
2. **Déployer sur Streamlit Cloud** :
   - Connectez-vous à [Streamlit Cloud](https://streamlit.io/cloud) avec votre compte GitHub.
   - Sélectionnez le dépôt que vous venez de créer.
   - Déployez l'application en suivant les instructions de Streamlit Cloud.

Si vous rencontrez des problèmes lors du déploiement ou avez besoin d'ajustements supplémentaires, n'hésitez pas à me le faire savoir !
""")
