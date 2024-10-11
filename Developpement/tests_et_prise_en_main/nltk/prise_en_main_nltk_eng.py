import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem import WordNetLemmatizer
from nltk import ne_chunk


textfr = """Je veux créer une fiche pédagogique. Programme de CM2 : l'histoire du musée du Louvre. Je veux des photos et du texte descriptif. Cette visite interactive permettra à vos élèves de découvrir des chefs-d'œuvre emblématiques, d'explorer différentes périodes historiques et d'enrichir leur compréhension du patrimoine culturel."""
#pour l'instant j'ai pas trouvé de modèle pré-entraîné pour le français, donc je vais utiliser un texte en anglais pour lo moment.
texteng = """I want to create an educational sheet. CM2 program: the history of the Louvre Museum. I want photos and descriptive text. This interactive visit will enable your students to discover emblematic masterpieces, explore different historical periods and enrich their understanding of cultural heritage."""
texteng2 = "The dogs are barking loudly in the park."


tokens = word_tokenize(texteng)
print(tokens)     # mot par mot
print(sent_tokenize(texteng)) # phrase par phrase
f = FreqDist(tokens) # fréquence des mots
print("les 3 mots les plus fréquents", f.most_common(3))   # les 3 mots les plus fréquents

tags = nltk.pos_tag(tokens)
print("les tags des mots sont:")
print(tags) # les tags des mots

lemmatizer = WordNetLemmatizer()
lemmas = [lemmatizer.lemmatize(token, pos = 'v') for token in tokens]   # sans le pos = 'v', lemmatizer.lemmatize ne pouvait pas transformer 'are' en 'be' et 'barking' en 'bark'
print("les lemmes des mots sont:", lemmas) # Réduction des mots à leur forme canonique (mot --> lemme)

without_stopwords = [word for word in tokens if word.lower() not in stopwords.words('english')]    # stop.words('english') est une liste de mots inutiles déjà prédéfinie par nltk
print("sans les mots inutiles:", without_stopwords) # sans les mots inutiles

print("les mots inutiles qui ont été enlevés sont:", set(tokens)-set(without_stopwords)) # voir les mots inutiles qui ont été enlevés

# identification des entités nommées dans notre exemple le musée du Louvre
ner_tags = ne_chunk(tags)
print(ner_tags)    




