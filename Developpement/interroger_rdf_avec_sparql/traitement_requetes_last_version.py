import spacy
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

nlp = spacy.load('fr_core_news_sm')
stopWords = set(stopwords.words('french'))
stemmer = SnowballStemmer(language='french')

test = "{Parle moi de Napoléon Bonaparte et de la bataille de Waterloo. Quand est-ce que la Seconde Guerre mondiale a eu lieu ?}"

# tokeniser une phrase
def return_token(sentence):
    doc = nlp(sentence)
    return [X.text for X in doc]

# Enlever les stop words
def remove_stop_words(tokens):
    return [token for token in tokens if token not in stopWords]

# tokenisation des phrases
def return_token_sent(sentence):
    doc = nlp(sentence)
    return [X.text for X in doc.sents]

# stemming
def return_stem(tokens):
    return [stemmer.stem(token) for token in tokens]

# reconnaissance d'entités nommées
def return_NER(sentence):
    doc = nlp(sentence)
    return [(X.text, X.label_) for X in doc.ents]

# Fonction complète pour traiter une requête textuelle en français
def process_text(sentence):
    # Tokenisation par phrases
    sentences = return_token_sent(sentence)
    processed_data = []

    for sent in sentences:

        tokens = return_token(sent)
        clean_tokens = remove_stop_words(tokens)
        stemmed_tokens = return_stem(clean_tokens)
        ner_entities = return_NER(sent)
        
        processed_data.append({
            'original_sentence': sent,
            'tokens': tokens,
            'clean_tokens': clean_tokens,
            'stemmed_tokens': stemmed_tokens,
            'ner_entities': ner_entities
        })
    
    return processed_data

processed_result = process_text(test)

for i, result in enumerate(processed_result):
    print(f"Phrase {i+1}: {result['original_sentence']}")
    print(f"Tokens: {result['tokens']}")
    print(f"Clean Tokens: {result['clean_tokens']}")
    print(f"Stemmed Tokens: {result['stemmed_tokens']}")
    print(f"Named Entities: {result['ner_entities']}")
    print("\n")
