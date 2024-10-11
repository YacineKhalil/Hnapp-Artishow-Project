#Installer Stanford Tagger : https://nlp.stanford.edu/software/tagger.shtml#Download

import nltk
from nltk.tag import StanfordPOSTagger



jar = '/Users/danielb/Downloads/stanford-postagger-full-2020-11-17/stanford-postagger.jar'
model = '/Users/danielb/Downloads/stanford-postagger-full-2020-11-17/models/french-ud.tagger'

pos_tagger = StanfordPOSTagger(model, jar, encoding = "utf-8")

words = nltk.word_tokenize("le chat mange la souris")
words2 = nltk.word_tokenize("Quelles villes sont localisées en Chine")
sentence = pos_tagger.tag(words)
sentence2 = pos_tagger.tag(words2)

print(sentence2)
grammar = r"""NP: {<DET>?<ADJ>*<NOUN>+}
               {<PRON>}
             
             
"""
cp = nltk.RegexpParser(grammar)

result = cp.parse(sentence2)
result.draw()