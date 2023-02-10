import spacy
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
print(sentence + " - ", similarity)




# I found that the similarities between the banana and the monkey was interesting because 
# i have no iea how this program would know that they liked bananas and i wonder whether this was
# put in by a human or whether it has learnt this itself

# A similarity i would suggest would be that banana and monkey have the same amount of letters in the name

# Using the different language model i noticed that with the SM model i am warned that
# the model has n tagger, parser and NER which may not give useful judgements. The similarity
# numbers are also a lot lower than the MD model which are mostly all above 0.8

