import nltk
import spacy # bibliotheque pour le français   
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem import WordNetLemmatizer
from nltk import ne_chunk
from nltk.stem.snowball import FrenchStemmer



textfr = """Je veux créer une fiche pédagogique. Programme de CM2 : l'histoire du musée du Louvre. Je veux des photos et du texte descriptif. Cette visite interactive permettra à vos élèves de découvrir des chefs-d'œuvre emblématiques, d'explorer différentes périodes historiques et d'enrichir leur compréhension du patrimoine culturel."""

nlp = spacy.load("fr_core_news_sm")
doc = nlp("Je veux créer une fiche pédagogique. Programme de CM2 : l'histoire du musée du Louvre. Je veux des photos et du texte descriptif. Cette visite interactive permettra à vos élèves de découvrir des chefs-d'œuvre emblématiques, d'explorer différentes périodes historiques et d'enrichir leur compréhension du patrimoine culturel.")

tokens = word_tokenize(textfr, language='french')
print(tokens)     # mot par mot
print(sent_tokenize(textfr, language='french')) # phrase par phrase
f = FreqDist(tokens) # fréquence des mots
print("les 3 mots les plus fréquents", f.most_common(3))   # les 3 mots les plus fréquents

# cette partie sur les tags ne supporte que l'anglais et le russe.
"""tags = nltk.pos_tag(tokens)
print("les tags des mots sont:")
print(tags) # les tags des mots"""
# alternative en français avec la bibliothèque spacy
for token in doc:
    print(token.text, token.pos_)

lemmatizer = WordNetLemmatizer()
lemmes = [lemmatizer.lemmatize(token) for token in tokens] 
stemmer = FrenchStemmer()
print("les lemmes des mots sont:", lemmes) # Réduction des mots à leur forme canonique (mot --> lemme)

without_stopwords = [word for word in tokens if word.lower() not in stopwords.words('french')]    # stop.words('french') est une liste de mots inutiles déjà prédéfinie par nltk
print("sans les mots inutiles:", without_stopwords) # sans les mots inutiles
print("les mots inutiles qui ont été enlevés sont:", set(tokens)-set(without_stopwords)) # voir les mots inutiles qui ont été enlevés

"""# identification des entités nommées 
ner_tags = ne_chunk(tags)
print(ner_tags)"""

# alternative en français avec la bibliothèque spacy
for entity in doc.ents:
    print(entity.text, entity.label_)

"""mots_de_demonstration = ["donner","don","donne","donnera","dons","test"]
stemmer = FrenchStemmer()
for w in mots_de_demonstration:
    print(stemmer.stem(w))"""

