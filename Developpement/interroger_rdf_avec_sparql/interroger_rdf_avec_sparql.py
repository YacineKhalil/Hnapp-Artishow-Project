import spacy
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from rdflib import Graph

# Charger le modèle de langue française de SpaCy
nlp = spacy.load('fr_core_news_sm')

# Charger la liste des stop words en français depuis NLTK
stopWords = set(stopwords.words('french'))

# Initialiser le stemmer Snowball pour le français
stemmer = SnowballStemmer(language='french')

# Fonction pour tokeniser une phrase
def return_token(sentence):
    doc = nlp(sentence)
    return [X.text for X in doc]

# Fonction pour enlever les stop words
def remove_stop_words(tokens):
    return [token for token in tokens if token not in stopWords]

# Fonction pour tokeniser par phrases
def return_token_sent(sentence):
    doc = nlp(sentence)
    return [X.text for X in doc.sents]

# Fonction pour appliquer le stemming
def return_stem(tokens):
    return [stemmer.stem(token) for token in tokens]

# Fonction pour la reconnaissance d'entités nommées (NER)
def return_NER(sentence):
    doc = nlp(sentence)
    return [(X.text, X.label_) for X in doc.ents]

# Fonction complète pour traiter une requête textuelle en français
def process_text(sentence):
    # Tokenisation par phrases
    sentences = return_token_sent(sentence)
    processed_data = []

    for sent in sentences:
        # Tokenisation
        tokens = return_token(sent)
        
        # Enlever les stop words
        clean_tokens = remove_stop_words(tokens)
        
        # Stemming
        stemmed_tokens = return_stem(clean_tokens)
        
        # Reconnaissance d'entités nommées
        ner_entities = return_NER(sent)
        
        # Rassembler les résultats pour la phrase actuelle
        processed_data.append({
            'original_sentence': sent,
            'tokens': tokens,
            'clean_tokens': clean_tokens,
            'stemmed_tokens': stemmed_tokens,
            'ner_entities': ner_entities
        })
    
    return processed_data

# Fonction pour générer une requête SPARQL
def generate_sparql_query(entities):
    sparql_query = """
    PREFIX dbo: <http://dbpedia.org/ontology/>
    PREFIX dbr: <http://dbpedia.org/resource/>
    SELECT ?subject ?predicate ?object
    WHERE {
    """
    
    conditions = []
    for entity, label in entities:
        if label in ['PER', 'ORG']:
            conditions.append(f"?subject ?predicate dbr:{entity.replace(' ', '_')}")
        elif label in ['LOC', 'EVENT']:
            conditions.append(f"?subject ?predicate ?object . FILTER(regex(str(?object), '{entity.replace(' ', '_')}', 'i'))")

    if conditions:
        sparql_query += " .\n".join(conditions)
        sparql_query += "\n}"
    else:
        sparql_query = ""

    return sparql_query

# Exemple de traitement et génération de requête SPARQL
def process_and_generate_sparql(query_text):
    # Traiter le texte
    processed_result = process_text(query_text)
    
    # Extraire les entités nommées
    entities = []
    for result in processed_result:
        entities.extend(result['ner_entities'])
    
    # Générer la requête SPARQL
    sparql_query = generate_sparql_query(entities)
    return sparql_query

# Exemple de requête textuelle
query_text = "parle moi de Napoléon et de la bataille de Waterloo"

# Traiter la requête et générer la requête SPARQL
sparql_query = process_and_generate_sparql(query_text)

# Afficher la requête SPARQL générée
print(sparql_query)

# Pour exécuter la requête SPARQL sur un graphe RDF
g = Graph()
g.parse("D:\\Cours\\Cycle_ingénieur\\proj104_artishow\\hnapp\\Developpement\\dataset_phrases_en_RDF\\dataset_en_rdf_new_version\\output1.rdf")  # Remplacez par le chemin de votre fichier RDF

if sparql_query:
    results = g.query(sparql_query)
    # Afficher les résultats de la requête SPARQL
    for row in results:
        print(row)
else:
    print("Aucune condition n'a été générée pour la requête SPARQL.")
