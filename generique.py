<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Effet de lecture dynamique</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            overflow: hidden;
            background-color: #111;
            color: #fff;
        }
        .text-container {
            position: relative;
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            overflow: hidden;
        }
        .text-content {
            position: absolute;
            top: 100%;
            animation: slide-down 10s infinite;
        }
        .text-reversed {
            position: absolute;
            bottom: -100%;
            animation: slide-up 10s infinite;
        }
        @keyframes slide-down {
            0% {
                top: 100%;
            }
            50% {
                top: 0%;
            }
            100% {
                top: -100%;
            }
        }
        @keyframes slide-up {
            0% {
                bottom: -100%;
            }
            50% {
                bottom: 0%;
            }
            100% {
                bottom: 100%;
            }
        }
        .text {
            padding: 10px;
            font-size: 2em;
            line-height: 1.5;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="text-container">
        <div class="text-content">
            <div class="text">La nouvelle offre d’acculturation à l’IA d’Inside est lancée.</div>
            <div class="text">Après 10 ans d’expertise dans la transformation digitale,</div>
            <div class="text">et une année entière d’exploration de l’intelligence artificielle,</div>
            <div class="text">la sensibilisation à l’IA semble se tasser.</div>
            <div class="text">Il serait naïf de croire que nous pouvons encore surprendre.</div>
            <div class="text">Comme vous le savez, l’enthousiasme finit toujours par s’éteindre.</div>
            <div class="text">Il est temps d’arrêter de dire que l’IA est l’avenir.</div>
            <div class="text">Certains pensent même que l’IA est une mode passagère.</div>
            <div class="text">Il est donc difficile de croire.</div>
            <div class="text">En termes de transformation digitale, cette offre est une révolution.</div>
        </div>
        <div class="text-reversed">
            <div class="text">Cette offre est une révolution en termes de transformation digitale.</div>
            <div class="text">Il est donc difficile de croire.</div>
            <div class="text">Certains pensent même que l’IA est l’avenir.</div>
            <div class="text">Il est temps d’arrêter de dire que l’enthousiasme finit toujours par s’éteindre.</div>
            <div class="text">Comme vous le savez, nous pouvons encore surprendre.</div>
            <div class="text">La sensibilisation à l’IA ne se tasse pas.</div>
            <div class="text">Après une année entière d’exploration de l’intelligence artificielle,</div>
            <div class="text">et 10 ans d’expertise dans la transformation digitale,</div>
            <div class="text">la nouvelle offre d’acculturation à l’IA d’Inside est lancée.</div>
            <div class="text">Cette offre est une révolution en termes de transformation digitale.</div>
        </div>
    </div>
</body>
</html>
