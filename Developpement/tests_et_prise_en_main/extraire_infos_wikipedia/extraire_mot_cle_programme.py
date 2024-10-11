# ce programme permet d'extraire les mots-clés (lemmes) d'un fichier pdf (contenant un programme pédagogique donné)

import fitz
import spacy
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nlp = spacy.load("fr_core_news_sm")

def extraire_texte_pdf(chemin_fichier_pdf):
    texte = ""
    with fitz.open(chemin_fichier_pdf) as document:
        for page in document:
            texte += page.get_text()
    return texte

chemin_pdf = "D:/Cours/Cycle_ingénieur/artishow_travail_local/programmes_pedagogiques/programme_seconde_generale.pdf"
texte_pdf = extraire_texte_pdf(chemin_pdf)

tokens = word_tokenize(texte_pdf, language='french')
#print(set(tokens)) 
without_stopwords = [word for word in tokens if word.lower() not in stopwords.words('french')]
#print("sans les mots inutiles:", set(without_stopwords))
#print("les mots inutiles qui ont été enlevés sont:", set(tokens)-set(without_stopwords))
doc = nlp(" ".join(without_stopwords))
lemmes = [word.lemma_ for word in doc]
print("les lemmes des mots sont:", set(lemmes))
#print("les entités nommées sont:", [ent.text for ent in doc.ents])     résulats pas du tout concluants

'''docbis = nlp(texte_pdf)
without_stopwords2 = [word for word in docbis if not word.is_stop]
without_stopwords2_pour_doc2 = [word.text for word in without_stopwords2]
doc2 = nlp(" ".join(without_stopwords2_pour_doc2))
lemmes2 = [word.lemma_ for word in doc2]
print("les lemmes des mots sont:", set(lemmes2)) # les mots utiles
print("--------------------------------------------------", set(lemmes2)-set(lemmes)) # les mots utiles qui ne sont pas des lemmes'''