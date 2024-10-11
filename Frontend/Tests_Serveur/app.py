from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/demarrer.html')
def demarrer():
    return render_template('demarrer.html')

@app.route('/result', methods=['POST'])
def result():
    query = request.form['query']
    # Exemple de traitement de la requête
    result = "Résultat de la requête : {}".format(query)
    return render_template('demarrer.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
