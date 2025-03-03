import re
from bnlp import BengaliCorpus as corpus


# Define the CleanText class
class TextCleaner:
    def __init__(self):
        punc = corpus.punctuations + ("‘") + ("’")
        self.PUNCTUATIONS = set(punc)
        self.STOPWORDS = set(corpus.stopwords)

    def remove_digits(self, text):
        return re.sub(r"[০-৯]+\d+", "", text).strip()

    def remove_punctuations(self, text, replace_with=" "):
        for punc in self.PUNCTUATIONS:
            text = text.replace(punc, replace_with)
        return " ".join(text.split())

    def remove_stopwords(self, text):
        words = text.split()
        new_text = [word for word in words if word.lower() not in self.STOPWORDS]
        return " ".join(new_text)

    def remove_english_and_special_chars(self, text):
        return re.sub(r'[a-zA-Z0-9!@#$%^&*()_+{}:;"\'<>,.?~\/-]+', "", text)
