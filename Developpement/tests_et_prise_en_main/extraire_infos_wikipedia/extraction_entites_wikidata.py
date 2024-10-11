import spacy
import requests

nlp = spacy.load("fr_core_news_sm")

def interroger_wikidata(entite):
    # Construction de la requête SPARQL
    sparql_query = """
    SELECT ?description WHERE {
      ?s rdfs:label "%s"@fr.
      ?s schema:description ?description.
      FILTER (lang(?description) = "fr")
    }
    """ % entite

    # Paramètres de la requête
    params = {
        "format": "json",
        "query": sparql_query
    }

    # Endpoint Wikidata
    endpoint_url = "https://query.wikidata.org/sparql"

    # Envoi de la requête SPARQL
    response = requests.get(endpoint_url, params=params)
    data = response.json()

    # Récupération de la description si disponible
    if data.get("results") and data["results"].get("bindings"):
        descriptions = [result["description"]["value"] for result in data["results"]["bindings"][0:100]]
        return descriptions
    else:
        return "Aucune information trouvée sur Wikidata pour cette entité."

def traiter_requete(requete):
    doc = nlp(requete)
    entites = [ent.text for ent in doc.ents]

    print("Entités nommées détectées : ", entites)
    
    # Interroger Wikidata pour chaque entité nommée
    for entite in entites:
        print("\nInformations sur", entite, ":\n")
        print(interroger_wikidata(entite))

def recevoir_requete():
    continuer = True
    while continuer:
        requete = input("Entrez votre requête en langage humain (ou entrez 'q' pour quitter) : ")
        if requete.lower() == 'q':
            continuer = False
        else:
            traiter_requete(requete)

if __name__ == "__main__":
    recevoir_requete()