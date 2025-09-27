#!/usr/bin/env python
"""
setup_nltk.py
Download the most commonly used NLTK datasets/models so your scripts run
without "LookupError: Resource not found". Safe to re-run.

Usage (Windows, from your project folder):
    python setup_nltk.py
"""

import sys
import nltk

# Core resources most scripts need
BASE_RESOURCES = [
    # tokenization
    "punkt",
    # stop words
    "stopwords",
    # lemmatization
    "wordnet", "omw-1.4",
    # POS tagging (name differs between NLTK versions)
    "averaged_perceptron_tagger", "averaged_perceptron_tagger_eng",
    # Named Entity Chunker + word list used by it
    "maxent_ne_chunker", "words",
]

# Frequently-used corpora (optional but handy for demos)
EXTRA_CORPORA = [
    "brown",
    "treebank",
    "conll2000",
    "movie_reviews",
    "vader_lexicon",
]

ALL = BASE_RESOURCES + EXTRA_CORPORA

def ensure(resource_id: str) -> bool:
    """
    Try to find the resource; if missing, download it.
    Returns True if the resource is available after this call.
    """
    try:
        # Map a few ids to their internal paths for nltk.data.find
        path_overrides = {
            "punkt": "tokenizers/punkt",
            "stopwords": "corpora/stopwords",
            "wordnet": "corpora/wordnet",
            "omw-1.4": "corpora/omw-1.4",
            "averaged_perceptron_tagger": "taggers/averaged_perceptron_tagger",
            "averaged_perceptron_tagger_eng": "taggers/averaged_perceptron_tagger_eng",
            "maxent_ne_chunker": "chunkers/maxent_ne_chunker",
            "words": "corpora/words",
            "brown": "corpora/brown",
            "treebank": "corpora/treebank",
            "conll2000": "corpora/conll2000",
            "movie_reviews": "corpora/movie_reviews",
            "vader_lexicon": "sentiment/vader_lexicon",
        }
        check_path = path_overrides.get(resource_id, resource_id)
        nltk.data.find(check_path)
        print(f"✓ Already present: {resource_id}")
        return True
    except LookupError:
        print(f"↓ Missing, downloading: {resource_id} ...")
        ok = nltk.download(resource_id, quiet=False, raise_on_error=False)
        if ok:
            print(f"✓ Downloaded: {resource_id}")
            return True
        else:
            print(f"✗ Failed: {resource_id}")
            return False

def main():
    print("=== NLTK Setup ===")
    print(f"NLTK version: {nltk.__version__}")
    print("Ensuring resources are available...\n")
    success, failed = [], []
    for rid in ALL:
        (success if ensure(rid) else failed).append(rid)

    print("\n=== Summary ===")
    if success:
        print("Available:", ", ".join(success))
    if failed:
        print("Failed   :", ", ".join(failed))
        print("\nIf a download failed, re-run this script or check your network/proxy.")
        print("You can also manually download via:")
        print(">>> import nltk; nltk.download()")

    # Exit code: 0 if all good, 1 if any failed
    sys.exit(0 if not failed else 1)

if __name__ == "__main__":
    main()
