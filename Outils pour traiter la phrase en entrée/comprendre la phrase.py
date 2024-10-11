import nltk
from nltk import FeatureChartParser, parse


# Grammaire formelle incluse dans le code, produit une requête SPARQL
list_pays = {"France": '?city wdt:P17 wd:Q148 . ?city wdt:P17 wd:Q142 .', "Chine": """?city wdt:P17 wd:Q148 . ?city wdt:P31 wd:Q515 .""" }


fcfg_grammar = """
% start S
S[SEM=(?np +' WHERE { '+ ?vp +' }')] -> NP[SEM=?np] VP[SEM=?vp]

VP[SEM=(?v + ?pp)] -> IV[SEM=?v] PP[SEM=?pp]
PP[SEM=(?p + ?np)] -> P[SEM=?p] NP[SEM=?np]

VP[SEM=(?v + ?ap)] -> IV[SEM=?v] AP[SEM=?ap]
NP[SEM=(?det + ?n)] -> Det[SEM=?det] N[SEM=?n]

AP[SEM=?pp] -> A[SEM=?a] PP[SEM=?pp]


Det[SEM='SELECT '] -> 'Quelles' | 'Quels' | 'Quelle' | 'Quel'
N[SEM='?city'] -> 'villes'
IV[SEM=''] -> 'sont'
A[SEM=''] -> 'localisées'
P[SEM=''] -> 'en'

"""
for i in list_pays:
    fcfg_grammar+="""NP[SEM='"""+list_pays[i]+"""'] -> '"""+i+ """'\n """
print(fcfg_grammar)


# Charger la grammaire directement depuis la chaîne de caractères
fcfg_parser = FeatureChartParser(nltk.grammar.FeatureGrammar.fromstring(fcfg_grammar), trace=3)

# Phrase à analyser
sentence = "Quelles villes sont localisées en Chine".split()

# Analyser la phrase
for tree in fcfg_parser.parse(sentence):
    sem = tree.label()['SEM']
    sparql_query = ''.join(sem)
    print(sparql_query)