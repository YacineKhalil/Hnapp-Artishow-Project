## Semaine finale

### Objectif : 

i) Faire un moteur de recherche à une entrée (un mot/concept) permettant de trouver toutes
les informations sur le mot entré dans le graphe sémantique construit à partir d'un manuel scolaire.

Les mots sont pré-définis - ce sont les noeuds du graphe (type : entity).

-> BFS avec un paramètre de distance

ii) Renvoyer les fiches / documents ayant un lien avec ces informations



### Déroulement :

1🚧) Construire le graphe sémantique pour chaque classe de niveau (CM1 etc ...)

1bis si possible) associer les uris wikidata à chaque noeud


2✅) Avoir un système de requêtes permettant d'associer des entrées textuelles à des noeuds du graphe
en python
(par exemple en entrant "Tra", renvoyer "Trafalgar" ...)

3) Avoir un système de requêtes permettant d'associer des entrées textuelles aux voisins du noeud
du graphe trouvé ( cf objectif 2) )
(par exemple en entrant "Tra", pouvoir sélectionner "Trafalgar" puis le système renvoie "Napoléon" ...)

BFS

> **SPARQL**
> 
> PREFIX ex: <http://example.org/>
> 
> SELECT DISTINCT ?neighbor
> WHERE {
>   {
>     ex:node ?predicate ?neighbor .
>   }
>   UNION
>   {
>     ?neighbor ?predicate ex:node .
>   }
> }