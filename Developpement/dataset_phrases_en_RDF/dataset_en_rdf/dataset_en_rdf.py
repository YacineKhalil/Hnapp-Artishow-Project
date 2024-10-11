import pandas as pd
import spacy
from rdflib import Graph, RDF, URIRef, Namespace

nlp = spacy.load("fr_core_news_md")
#df = pd.read_csv("D:\\Cours\\Cycle_ingénieur\\proj104_artishow\\hnapp\\Developpement\\graphe_de_connaissances\\phrases_de_test.csv", encoding="ISO-8859-1")

EX = Namespace("http://example.org/")

g = Graph()
g.bind("ex", EX)

# Fonction pour créer des URI uniques
def create_uri(entity):
    return URIRef(EX + entity.replace(" ", "_"))

def extract_entities_relations(text):
    doc = nlp(text)
    entities = [ent.text for ent in doc.ents]
    return entities

df['entities'] = df['phrase'].apply(extract_entities_relations)

for _, row in df.iterrows():
    entities = row['entities']
    for entity in entities:
        g.add((create_uri(entity), RDF.type, EX.Entity))

for _, row in df.iterrows():
    entities = row['entities']
    for i, entity1 in enumerate(entities):
        for j, entity2 in enumerate(entities):
            if i != j:
                # Ajouter la relation entre les entités
                relation_uri = URIRef(EX + "relation_" + str(i) + "_" + str(j))
                g.add((create_uri(entity1), relation_uri, create_uri(entity2)))

# Sauvegarder le graphe en RDF/XML
g.serialize("D:\\Cours\\Cycle_ingénieur\\proj104_artishow\\hnapp\\Developpement\\dataset_phrases_en_RDF\\test3.rdf", format="xml")
