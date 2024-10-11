from rdflib import Graph

def construct_sparql_label_query(input_string):
    # PREFIX a modifier avec le rdf qu'on a construit
    '''
    Construction de la requête SPARQL
    '''
    
    sparql_query = """
    PREFIX ex: <http://example.org/>

    SELECT ?node ?name
    WHERE {
        ?node ex:name ?name .
        FILTER (STRSTARTS(LCASE(STR(?name)), '""" + input_string.lower() + """'))
    }
    """

    return sparql_query

def main(rdf_graph):
    user_query = input("Entrez le sujet de votre recherche")
    
    # Construction de la requête SPARQL
    sparql_query = construct_sparql_label_query(user_query)
    print("Generated SPARQL Query:\n", sparql_query)
    
    # Interrogation du RDF
    results = rdf_graph.query(sparql_query)
    
    # Affichage de la réponse
    response_names=[]
    for row in results:
        name=row[1]
        response_names.append(name)
        print(name)

if __name__ == "__main__":

    # Chargement du fichier RDF
    rdf_file = "example.rdf"  # A spécifier une fois sur le serveur
    graph = Graph()
    graph.parse(rdf_file, format="xml") # Sur le serveur, il faut se débrouiller pour que cette étape ne se répète pas tout le temps
    #typiquement en ouvrant un graph par manuel dans ce processus et en ajoutant un paramètre dans le moteur de recherche

    # Traitement d'une requête
    main(graph)
