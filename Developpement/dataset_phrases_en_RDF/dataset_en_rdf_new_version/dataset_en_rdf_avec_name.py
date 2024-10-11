import pandas as pd
import spacy
from spacy.matcher import Matcher
from rdflib import Graph, RDF, URIRef, Namespace, Literal

nlp = spacy.load("fr_core_news_sm")

EX = Namespace("http://example.org/")

g = Graph()
g.bind("ex", EX)

# Fonction pour créer des URI uniques
def create_uri(entity):
    return URIRef(EX + entity.replace(" ", "_"))

def extract_entities_relations(text):
    doc = nlp(text)
    entities = [ent.text for ent in doc.ents]
    
    relations = []
    matcher = Matcher(nlp.vocab)

    # Définir la structure de la relation
    pattern = [{'DEP':'ROOT'}, 
               {'DEP':'prep','OP':"?"},
               {'DEP':'agent','OP':"?"},  
               {'POS':'ADJ','OP':"?"}] 

    matcher.add("matching_1", [pattern]) 
    matches = matcher(doc)
    if matches:
        k = len(matches) - 1
        span = doc[matches[k][1]:matches[k][2]] 
        relation = span.text
    else:
        relation = None
    return entities, relation

#df = pd.read_csv("D:\\Cours\\Cycle_ingénieur\\proj104_artishow\\hnapp\\Developpement\\graphe_de_connaissances\\phrases_de_test.csv", encoding="ISO-8859-1")
#df = pd.read_csv("D:\\Cours\\Cycle_ingénieur\\proj104_artishow\\hnapp\\Developpement\\traitement_pdfs\\manuels_et_cours\\CM1\\test_reussis\\histoire_cm1.csv", encoding="ISO-8859-1")
df = pd.read_csv("D:\\Cours\\Cycle_ingénieur\\proj104_artishow\\hnapp\\Developpement\\traitement_pdfs\\manuels_et_cours\\CM2\\histoire_cm2.csv", encoding="ISO-8859-1")

for _, row in df.iterrows():
    entities, relation = extract_entities_relations(row['phrase'])
    print(entities, relation)
    
    for entity in entities:
        entity_uri = create_uri(entity)
        g.add((entity_uri, RDF.type, EX.Entity))
        g.add((entity_uri, EX.name, Literal(entity)))  # Ajout de l'étiquette <ex:name>
    
    if relation:
        for i, entity1 in enumerate(entities):
            for j, entity2 in enumerate(entities):
                if i != j:
                    g.add((create_uri(entity1), URIRef(EX + relation.replace(" ", "_")), create_uri(entity2)))

#g.serialize("D:\\Cours\\Cycle_ingénieur\\proj104_artishow\\hnapp\\Developpement\\dataset_phrases_en_RDF\\dataset_en_rdf_new_version\\output2.rdf", format="xml")
#g.serialize("D:\\Cours\\Cycle_ingénieur\\proj104_artishow\\hnapp\\Developpement\\traitement_pdfs\\manuels_et_cours\\CM1\\test_reussis\\histoire_cm1_new.rdf", format="xml")
g.serialize("D:\\Cours\\Cycle_ingénieur\\proj104_artishow\\hnapp\\Developpement\\traitement_pdfs\\manuels_et_cours\\CM2\\histoire_cm2_new.rdf", format="xml")