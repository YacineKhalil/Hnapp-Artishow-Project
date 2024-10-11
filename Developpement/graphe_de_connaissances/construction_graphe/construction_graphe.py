# ce code permet de construire un graphe de connaissances à partir d'un fichier csv contenant des phrases en français 
# et de les analyser pour en extraire les entités et les relations entre ces entités.
# L'objectif étant pour la suite de convertir les programmes pédagogiques en graphe de connaissances pour faciliter leur exploitation
# et donc avant cela de les convertir en fichier csv de phrases séparées contenant un sujet, verbe complément comme structure de base.

import pandas as pd
import spacy
from spacy.matcher import Matcher  
import networkx as nx
import matplotlib.pyplot as plt
from tqdm import tqdm
import pandas as pd

pd.set_option('display.max_colwidth', 200)
nlp = spacy.load('fr_core_news_sm')
csv_file_path = "D:\\Cours\\Cycle_ingénieur\\proj104_artishow\\hnapp\\Developpement\\graphe_de_connaissances\\dataset_programme.csv"
candidate_sentences = pd.read_csv(csv_file_path, encoding='latin1')
candidate_sentences.shape

def get_entities(sent):
    ent1 = ""
    ent2 = ""
    for tok in nlp(sent):
        if tok.dep_ == "nsubj":
            ent1 = " ".join([tok.text_with_ws] + [child.text for child in tok.children if child.dep_ != "det"])
        elif tok.dep_ == "obj":
            ent2 = " ".join([tok.text_with_ws] + [child.text for child in tok.children if child.dep_ != "det"])  

    return [ent1.strip(), ent2.strip()]

def relation(sent):
  doc = nlp(sent)
  matcher = Matcher(nlp.vocab)

  # définir la structure de la relation, j'ai essayé plusieurs structures et celle-ci est la plus efficace jusqu'à présent quoique toujours pas parfaite
  pattern = [{'DEP':'ROOT'}, 
            {'DEP':'prep','OP':"?"},
            {'DEP':'agent','OP':"?"},  
            {'POS':'ADJ','OP':"?"}] 

  matcher.add("matching_1", [pattern]) 
  matches = matcher(doc)
  k = len(matches) - 1
  span = doc[matches[k][1]:matches[k][2]] 
  return(span.text)

#print(get_entities("le film a eut 200 patentes en 2020"))   # test

entity_pairs = []
for i in tqdm(candidate_sentences["Phrase"]):
  entity_pairs.append(get_entities(i))
print(entity_pairs)

#print(relation("Lucas conduit la voiture"))   # test

relations = [relation(i) for i in tqdm(candidate_sentences['Phrase'])]
print(pd.Series(relations).value_counts()[:50])

# construction du graphe de connaissances
départ = [i[0] for i in entity_pairs]
arrivée = [i[1] for i in entity_pairs]
kg_df = pd.DataFrame({'départ':départ, 'arrivée':arrivée, 'arrête':relations})

# afficher tout le graphe
G=nx.from_pandas_edgelist(kg_df, "départ", "arrivée", edge_attr=True, create_using=nx.MultiDiGraph())
plt.figure(figsize=(12,12))
pos = nx.spring_layout(G)
nx.draw(G, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues, pos = pos)
plt.show()

# n'afficher que les relation dy type "opposé"
G=nx.from_pandas_edgelist(kg_df[kg_df['arrête']=="opposé"], "départ", "arrivée", edge_attr=True, create_using=nx.MultiDiGraph())
plt.figure(figsize=(12,12))
pos = nx.spring_layout(G, k = 0.5) # k regulates the distance between nodes
nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, edge_cmap=plt.cm.Blues, pos = pos)
plt.show()

# n'afficher que les relation dy type "marqué"
G=nx.from_pandas_edgelist(kg_df[kg_df['arrête']=="marqué"], "départ", "arrivée", edge_attr=True, create_using=nx.MultiDiGraph())
plt.figure(figsize=(12,12))
pos = nx.spring_layout(G, k = 0.5) # k regulates the distance between nodes
nx.draw(G, with_labels=True, node_color='green', node_size=1500, edge_cmap=plt.cm.Blues, pos = pos)
plt.show()