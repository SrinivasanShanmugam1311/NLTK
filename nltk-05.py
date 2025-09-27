from nltk import pos_tag
from nltk.tokenize import word_tokenize
import nltk
nltk.download('averaged_perceptron_tagger_eng')
sentence = "NLTK provides powerful text processing libraries."
tokens = word_tokenize(sentence)
print(pos_tag(tokens))
