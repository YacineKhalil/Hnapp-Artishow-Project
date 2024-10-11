import spacy
import csv
import codecs

# Chargement du modèle spaCy pour le français
nlp = spacy.load('fr_core_news_sm')

# Fonction pour lire le fichier texte avec codecs
def read_text_file(file_path):
    with codecs.open(file_path, 'r', encoding='utf-8-sig') as file:
        return file.read()

# Fonction pour tokeniser les phrases (tirée de votre code)
def return_token_sent(sentence):
    doc = nlp(sentence)
    return [X.text for X in doc.sents]

# Fonction pour écrire les phrases dans un fichier CSV avec codecs
def write_sentences_to_csv(sentences, output_file):
    with codecs.open(output_file, 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['sentence'])  # Écrire l'en-tête
        for sentence in sentences:
            writer.writerow([sentence.strip()])  # Écrire chaque phrase dans une ligne

# Chemin du fichier texte d'entrée et du fichier CSV de sortie
input_file = 'D:\\Cours\\Cycle_ingénieur\\proj104_artishow\\hnapp\\Developpement\\traitement_pdfs\\manuels_et_cours\\CM1\\test_reussis\\CM1.txt'
output_file = 'D:\Cours\Cycle_ingénieur\proj104_artishow\hnapp\Developpement\\traitement_pdfs\manuels_et_cours\CM1\\test_reussis\\CM1_new(3).csv'

# Lecture du fichier texte
text_content = read_text_file(input_file)

# Séparation du texte en phrases en utilisant la fonction donnée
sentences = return_token_sent(text_content)

# Écriture des phrases dans le fichier CSV
write_sentences_to_csv(sentences, output_file)

print(f"Le contenu a été séparé en phrases et enregistré dans {output_file}")
