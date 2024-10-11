http = require("http")
fs = require("fs")
const express = require('express');
const { exec } = require('child_process');

const app = express();
const port = 3000;

app.use(express.json());

app.post('/execute-python', (req, res) => {
    const { code } = req.body;

    // Exécuter le code Python
    exec(`python -c "${code}"`, (error, stdout, stderr) => {
        if (error) {
            console.error(`Erreur d'exécution : ${error.message}`);
            res.status(500).send('Erreur lors de l\'exécution du code Python');
            return;
        }
        if (stderr) {
            console.error(`Erreur de sortie : ${stderr}`);
            res.status(400).send(stderr);
            return;
        }
        console.log(`Résultat : ${stdout}`);
        res.send(stdout);
    });
});

app.listen(port, () => {
    console.log(`Serveur démarré sur http://localhost:${port}`);
});

/*
Ce code crée un serveur Express qui écoute sur le port 3000. 
Il expose une seule route POST /execute-python qui attend un objet JSON avec une propriété code. 
Le serveur exécutera ensuite le code Python fourni et renverra le résultat

Pour tester le serveur : installer node et exécuter la commande node server.js sur le terminal

POUR ENVOYER DES DONNEES : on envoie un objet JSON dans une requête POST.
http://adrienjoly.com/cours-javascript/tp12.html

*/