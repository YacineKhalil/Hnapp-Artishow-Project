#Point d'entrée vers WDQS depuis python
from SPARQLWrapper import SPARQLWrapper, JSON


sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
sparql.setReturnFormat(JSON)


sparql.setQuery("""SELECT ?item ?fcode ?jhcode WHERE { ?item wdt:P31 wd:Q3305213 ; p:P170/ps:P170 wd:Q5582 . MINUS { ?item wdt:P31 wd:Q18761202 } . OPTIONAL {?item p:P528 [ps:P528 ?fcode ; pq:P972 wd:Q17280421 ]. } OPTIONAL {?item p:P528 [ps:P528 ?jhcode ; pq:P972 wd:Q19833315 ] . } } LIMIT 100""")

sparql.setQuery(q)

#Affiche le résultat de la requête sparql : 
try:
    ret = sparql.queryAndConvert()
    
    print(ret["results"])
    for r in ret["results"]["bindings"]:
        print(r)
except Exception as e:
    print(e)