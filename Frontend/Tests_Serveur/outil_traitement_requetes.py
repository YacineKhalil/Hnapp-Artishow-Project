import spacy
import wikipediaapi

# Initialiser l'API Wikipedia avec un agent utilisateur spécifié
wiki = wikipediaapi.Wikipedia(
    language='fr',
    extract_format=wikipediaapi.ExtractFormat.WIKI,
    user_agent="MyWikiBot/0.1 (https://gitlab.telecom-paris.fr/yacine.khalil/testwikibot/)"
)

nlp = spacy.load("fr_core_news_sm")

def obtenir_infos_wikipedia(entite):
    page = wiki.page(entite)
    if page.exists():
        return page.summary
    else:
        return "Aucune information trouvée sur Wikipedia pour cette entité."

def traiter_requete(requete):

    doc = nlp(requete)
    entites = [ent.text for ent in doc.ents]

    print("Entités nommées détectées : ", entites)
    
    # Rechercher des informations sur Wikipedia pour chaque entité nommée
    for entite in entites:
        print("\nInformations sur", entite, ":\n")
        print(obtenir_infos_wikipedia(entite))

def recevoir_requete():
    requete = input("Entrez votre requête en langage humain : ")
    traiter_requete(requete)

if __name__ == "__main__":
    recevoir_requete()