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
    
    def remove_emojis(self, text):
        # Unicode ranges for emojis
        emoji_pattern = re.compile(
            "["
            "\U0001F600-\U0001F64F"  # emoticons
            "\U0001F300-\U0001F5FF"  # symbols & pictographs
            "\U0001F680-\U0001F6FF"  # transport & map symbols
            "\U0001F700-\U0001F77F"  # alchemical symbols
            "\U0001F780-\U0001F7FF"  # Geometric Shapes
            "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
            "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
            "\U0001FA00-\U0001FA6F"  # Chess Symbols
            "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
            "\U00002702-\U000027B0"  # Dingbats
            "\U000024C2-\U0001F251" 
            "]+", flags=re.UNICODE
        )
        return emoji_pattern.sub(r'', text)
