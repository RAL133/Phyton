import spacy 

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
counter = 0
stopcounter = 0
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)
    if token.is_stop == False:
        counter += 1
    else:
        stopcounter += 1

print(f'number of stopwords: {stopcounter}, number of non-stop words: {counter}')