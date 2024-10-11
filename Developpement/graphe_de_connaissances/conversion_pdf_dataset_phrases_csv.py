"""import fitz
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

chemin_pdf = "D:\\Cours\\Cycle_ingénieur\\proj104_artishow\\hnapp\\Programmes scolaires\\manuel-histoire-cm2.pdf"
phrases_pdf = extraire_phrases_pdf(chemin_pdf)

for phrase in phrases_pdf:
    print(phrase)        """

import csv
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as document:
        for page in document:
            text += page.get_text()
    return text

def save_text_to_csv(text, csv_path):
    # Diviser le texte en phrases
    phrases = text.split('.')
    # Écrire les phrases dans un fichier CSV
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for phrase in phrases:
            writer.writerow([phrase.strip()])

# Chemin vers le PDF
chemin_pdf = "D:\\Cours\\Cycle_ingénieur\\artishow_travail_local\\programmes_pedagogiques\\manuel histoire pretraite.pdf"

# Extraire le texte du PDF
texte_pdf = extract_text_from_pdf(chemin_pdf)

# Chemin pour enregistrer le fichier CSV
chemin_csv = "D:\\Cours\\Cycle_ingénieur\\proj104_artishow\\hnapp\\Developpement\\graphe_de_connaissances\\texte_phrases.csv"

# Enregistrer les phrases dans un fichier CSV
save_text_to_csv(texte_pdf, chemin_csv)


import pdfplumber
import csv

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def save_text_to_csv(text, csv_path):
    with open(csv_path, 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for sentence in text.split('.'):
            writer.writerow([sentence.strip()])

# Chemin vers votre fichier PDF
chemin_pdf = "chemin/vers/votre/fichier.pdf"
texte_pdf = extract_text_from_pdf(chemin_pdf)

# Enregistrer le texte extrait dans un fichier CSV
chemin_csv = "chemin/vers/votre/fichier.csv"
save_text_to_csv(texte_pdf, chemin_csv)


