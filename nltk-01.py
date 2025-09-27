import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

text = "NLTK is a leading platform for building Python programs to work with human language data."

print("Word Tokens:", word_tokenize(text))
print("Sentence Tokens:", sent_tokenize(text))
