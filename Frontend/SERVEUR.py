from flask import Flask, request, render_template, redirect, send_file
import os
import sys
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('demarrer.html')


@app.route("/traitement", methods=["POST"])
def traitement():
    donnees = request.form
    texte = donnees.get('q')
    #print(texte)
    #A faire ensuite : Traitement(texte)

    from nltk import load_parser
    from nltk.sem import chat80
    cp = load_parser('grammars/book_grammars/sql0 copie.fcfg')
    query = texte
    trees = list(cp.parse(query.split()))
    answer = trees[0].label()['SEM']
    answer = [s for s in answer if s]
    q = ' '.join(answer)
    print(q)




    #La fonction Traitement(texte) nous retourne un fichier PDF à placer dans le dossier Frontend !


    #Retourne le fichier FICHE.pdf : 
    with open(os.path.join('FICHE.pdf'), 'rb') as static_file:
        return send_file(static_file, attachment_filename='FICHE.pdf')

    
        



if __name__ == '__main__':
    app.run(debug=True,port=8000)
