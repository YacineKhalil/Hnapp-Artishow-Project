import sys
import json

from rdflib import Graph
import sparql_queries


def search_labels(query,rdf_graph):
    """search for entities whose name (ex:name) matches the query in the rdf file
    if a match is found, returns the names of the neighbours of the match
    if not, returns the names of entities that have a ressembling name"""

    # Search for (exact) name-matching entities in the rdf file
    exact_label_query=sparql_queries.exact_label_query(query)
    exact_label_results = rdf_graph.query(exact_label_query)

    if len( exact_label_results ) != 0:
        query_match=True
        neighbour_query=sparql_queries.neighbours_query(query)
        neighbour_results=rdf_graph.query(neighbour_query)
        neighbour_response=[]

        if len( neighbour_results ) != 0:
            neighbour_match=True
            for row in neighbour_results:
                relation , name = row[0][19:] , row[1]  #[19:] <-> enlever le préfixe
                neighbour_response.append(name + " : " + relation)
        else:
            neighbour_match=False

        return (query_match,neighbour_match,neighbour_response)
    
    else:
        # Search for (inexact, meaning string containing the query) name-matching entities in the rdf file
        query_match=False
        neighbour_match=False
        inexact_label_query=sparql_queries.inexact_label_query(query)
        inexact_label_results = rdf_graph.query(inexact_label_query)
        inexact_response_names=[]

        for row in inexact_label_results:
            name=row[1] #0 : node, 1 : name
            inexact_response_names.append(name)
        return (query_match,neighbour_match,inexact_response_names)

if __name__ == '__main__':

    dic_rdf_file = {"cm1":"histoire_cm1_new.rdf","cm2":"histoire_cm2_new.rdf","":"histoire_merged_new.rdf"}
    graph = Graph()

# Traitement d'une requête
    arg = sys.argv
    query = arg[1]
    category = arg[2]

    # En fonction de la classe choisie
    if category in dic_rdf_file:
        rdf_file = dic_rdf_file[category]
    else:
        rdf_file = dic_rdf_file["histoire_merged_new.rdf"]  #essayer de construie un graphe réunissant toutes les classes

    graph.parse(rdf_file, format="xml") # Sur le serveur, il faut se débrouiller pour que cette étape ne se répète pas tout le temps
    #typiquement en ouvrant un graph par manuel dans ce processus et en ajoutant un paramètre dans le moteur de recherche
    answer=search_labels(query,graph)
    query_match,neighbour_match,results = answer[0],answer[1],answer[2]

    if query_match:
        if neighbour_match:
            print(json.dumps( ["Votre recherche a les liens suivants :"] + results ))
        else:
            print(json.dumps( ["Votre recherche est au programme mais sans lien trouvé :"] + results ))
    else:
        if len( results )!=0:
            print(json.dumps( ["Vouliez-vous dire :"] + results ))
        else:
            print(json.dumps( ["Aucune correspondance trouvée dans ce programme"] + results ))