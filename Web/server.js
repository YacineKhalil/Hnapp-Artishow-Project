const express = require('express');
const bodyParser = require('body-parser');
const { exec } = require('child_process');

const app = express();
const port = 3000;

// Use body-parser middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Serve static files (HTML, CSS, JS) from the 'public' directory
app.use(express.static('public'));

// API endpoint to execute the Python script
app.post('/search', (req, res) => {
    const query = req.body.query;
    const category = req.body.category;

    // Execute the Python script with the query as an argument
    exec(`python3 search.py "${query}" "${category}"`, (error, stdout, stderr) => {
        if (error) {
            console.error(`Execution error: ${error.message}`);
            res.status(500).send('Error executing Python script');
            return;
        }
        if (stderr) {
            console.error(`Execution error: ${stderr}`);
            res.status(400).send(stderr);
            return;
        }
        res.send(stdout);
    });
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});


/*
Pour tester le serveur : installer node et exécuter la commande node server.js sur le terminal
*/