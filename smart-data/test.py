import spacy

nlp = spacy.load("en")
doc = nlp("This hotel is truly huge and beautiful. I'll be back for sure")


# doc = nlp("I'll code code")
# for word in doc:
#     print(word.text, word.lemma_, word.pos_)

# I -PRON- PRON
# 'll will VERB
# code code VERB
# code code NOUN

woman, lady, dude = nlp("woman lady dude")
woman.similarity(lady)  # 0.78
woman.similarity(dude)  # 0.40
