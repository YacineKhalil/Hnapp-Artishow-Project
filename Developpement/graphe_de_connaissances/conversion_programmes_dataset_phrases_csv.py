import fitz
import spacy

nlp = spacy.load("fr_core_news_sm")

def extraire_phrases_pdf(chemin_fichier_pdf):
    phrases = []
    with fitz.open(chemin_fichier_pdf) as document:
        for page in document:
            texte = page.get_text()
            doc = nlp(texte)
            for sent in doc.sents:
                phrases.append(sent.text.strip())
    return phrases

chemin_pdf = "D:/Cours/Cycle_ingénieur/artishow_travail_local/programmes_pedagogiques/programme_seconde_generale.pdf"
phrases_pdf = extraire_phrases_pdf(chemin_pdf)

for phrase in phrases_pdf:
    print(phrase)
