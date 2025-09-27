from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
words = ["running", "runner", "runs", "easily", "fairly"]
print([stemmer.stem(w) for w in words])
