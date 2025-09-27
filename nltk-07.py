from nltk.util import ngrams
from nltk.tokenize import word_tokenize

sentence = "I love natural language processing"
tokens = word_tokenize(sentence)
bigrams = list(ngrams(tokens, 3))
print(bigrams)
