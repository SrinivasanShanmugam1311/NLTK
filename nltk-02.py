from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

words = word_tokenize("This is a simple example to remove stopwords from text using NLTK.")
filtered = [w for w in words if w.lower() not in stopwords.words('english')]
print(filtered)
