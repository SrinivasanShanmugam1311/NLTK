from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize

text = "NLTK makes text processing simple and fun. Text processing is important."
tokens = word_tokenize(text.lower())
fdist = FreqDist(tokens)
print(fdist.most_common(5))
fdist.plot(5)
