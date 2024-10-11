from rdflib import Graph

def exact_label_query(input_string):
    # PREFIX a modifier avec le rdf qu'on a construit
    '''
    Construction de la requête SPARQL pour trouver des correspondances exactes de label avec l'input dans le rdf
    '''
    
    sparql_query = """
    PREFIX ex: <http://example.org/>

    SELECT ?uri ?name
    WHERE {
        ?uri ex:name ?name .
        FILTER (LCASE(STR(?name))='""" + input_string.lower() + """')
    }
    LIMIT 10
    """

    return sparql_query

def inexact_label_query(input_string):
    # PREFIX a modifier avec le rdf qu'on a construit
    # On pourrait tenter d'utiliser la distance de levenshtein aussi
    '''
    Construction de la requête SPARQL pour trouver des correspondances inexactes de label avec l'input dans le rdf
    '''
    
    sparql_query = """
    PREFIX ex: <http://example.org/>

    SELECT ?uri ?name
    WHERE {
        ?uri ex:name ?name .
        FILTER (CONTAINS(LCASE(STR(?name)), '""" + input_string.lower() + """'))
    }
    LIMIT 10
    """

    return sparql_query

def neighbours_query(input_string):
    # PREFIX a modifier avec le rdf qu'on a construit
    '''
    Construction de la requête SPARQL pour trouver les labels de tous les voisins de noeuds dont le label est l'input
    Toutes les relations sont symétriques
    '''
    
    sparql_query = """
    PREFIX ex: <http://example.org/>

    SELECT ?relation ?nameneighbour
    WHERE {
        ?uri ex:name ?name .
        FILTER (LCASE(STR(?name))='""" + input_string.lower() + """') .
        ?urineighbour ?relation ?uri .
        ?urineighbour ex:name ?nameneighbour
    }
    LIMIT 10
    """

    return sparql_query