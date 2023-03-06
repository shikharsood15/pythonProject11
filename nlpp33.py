#named entity recognition
# import en_core_web_sm
# import spacy.cli
# spacy.cli.download("en_core_web_lg")
# from spacy.lang.en import English
# nlp=English()
# import en_core_web_sm
# import en_core_web_md

import spacy
from spacy import displacy
import spacy.cli
from spacy import tokenizer
# spacy.cli.download("en_core_web_sm")
nlp = spacy.load("en_core_web_sm")


# nlp = spacy.load('en_core_web_sm')

#Load the text and process it
# I copied the text from python wiki
text ="""Python is an interpreted, high-level and general-purpose programming language"
       "Pythons design philosophy emphasizes code readability with"
       "its notable use of significant indentation."
       "Its language constructs and object-oriented approach aim to"
       "help programmers write clear and"
       "logical code for small and large-scale projects"""
# text2 = # copy the paragraphs from  https://www.python.org/doc/essays/
doc = nlp(text)
#doc2 = nlp(text2)
# sentences = list(doc.sents)
# print(sentences)
# tokenization
# for token in doc:
#     print(token.text)
# print entities
# ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]
# print(ents)
print(doc)
for ent in doc.ents:
              print(ent.text, ent.start_char, ent.end_char, ent.label_)
# now we use displaycy function on doc2
# displacy.render(doc, style='ent', jupyter=True)



# https://www.geeksforgeeks.org/named-entity-recognition/

#
#
# import nltk
# nltk.download('words')
# nltk.download('punkt')
# nltk.download('maxent_ne_chunker')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('state_union')
# from nltk.corpus import state_union
# from nltk.tokenize import PunktSentenceTokenizer
#
# # process the text and print Named entities
# # tokenization
# train_text = state_union.raw()
#
# sample_text = state_union.raw("2006-GWBush.txt")
# custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
# tokenized = custom_sent_tokenizer.tokenize(sample_text)
# # function
# def get_named_entity():
#     try:
#         for i in tokenized:
#             words = nltk.word_tokenize(i)
#             tagged = nltk.pos_tag(words)
#             namedEnt = nltk.ne_chunk(tagged, binary=False)
#             namedEnt.draw()
#     except:
#         pass
# get_named_entity()
