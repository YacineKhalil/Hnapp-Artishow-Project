from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph, Namespace, Literal

# Fonction pour interroger WIKIDATA avec SPARQL
def query_wikidata(query):
    sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results

# Fonction pour charger les données RDF du programme pédagogique
def load_programme_rdf(filename):
    g = Graph()
    with open(filename, 'rb') as f:
        g.parse(file=f, format='turtle')  # Charger le fichier RDF
    return g

# Requête SPARQL pour récupérer des informations sur la Tour Eiffel depuis WIKIDATA
sparql_query = """
SELECT DISTINCT ?propertyLabel ?valueLabel WHERE {
  wd:Q243 ?property ?value .
  ?property wikibase:directClaim ?propertyId .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
"""

# Interroger WIKIDATA avec la requête SPARQL
wikidata_results = query_wikidata(sparql_query)

# Charger les données RDF du programme pédagogique CM2
programme_rdf = load_programme_rdf("D:/Cours/Cycle_ingénieur/proj104_artishow/hnapp/programme_cm2_test.rdf")

# Récupérer les triples RDF concernant la Tour Eiffel dans le programme pédagogique CM2
tour_eiffel_triples = programme_rdf.triples((None, Namespace("http://example.org/").topic, Namespace("http://example.org/").TourEiffel))

# Afficher les résultats
print("Informations sur la Tour Eiffel depuis WIKIDATA:")
for result in wikidata_results["results"]["bindings"]:
    print(result["propertyLabel"]["value"] + ":", result["valueLabel"]["value"])

print("\nOccurrence(s) de la Tour Eiffel dans le programme pédagogique CM2:")
for triple in tour_eiffel_triples:
    print("Sujet:", triple[0])
    print("Prédicat:", triple[1])
    print("Objet:", triple[2])
