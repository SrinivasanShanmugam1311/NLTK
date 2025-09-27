from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
words = ["running", "better", "geese", "studies"]
print([lemmatizer.lemmatize(w) for w in words])
