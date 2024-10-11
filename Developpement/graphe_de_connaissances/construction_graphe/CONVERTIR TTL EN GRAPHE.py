#Transforme un fichier .ttl en graphe qu'on peut visualiser :



from rdflib import Graph
import networkx as nx
from rdflib import Namespace
from rdflib.namespace import NamespaceManager
import matplotlib.pyplot as plt

G = nx.DiGraph()
g = Graph()

g.parse("hda_data_2023-03-27T050001_0.1.ttl", format="turtle")

i=0

for subj, pred, obj in g:
    if i == 30:
        break
        
        
    
    G.add_node(subj)
    G.add_node(pred)
    G.add_node(obj)
    
    G.add_edge(subj,pred)
    G.add_edge(pred,obj)
    
    i=i+1

plt.figure(figsize=(12,12))
pos = nx.spring_layout(G,k=100, scale=1000)
nx.draw(G, with_labels=True, node_color='green', node_size=150, edge_cmap=plt.cm.Blues, pos = pos)
plt.show()

