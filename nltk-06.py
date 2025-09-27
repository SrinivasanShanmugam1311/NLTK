from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree

import nltk
nltk.download('maxent_ne_chunker_tab')
sentence = "Barack Obama was the 44th President of the United States."
chunked = ne_chunk(pos_tag(word_tokenize(sentence)))
print(chunked)
