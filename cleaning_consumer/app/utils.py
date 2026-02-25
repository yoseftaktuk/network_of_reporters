import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class CleaningService:
    def __init__(self):   
        nltk.download('stopwords')
        nltk.download('punkt_tab')
    def punctuation_cleaning(self, words: str):
        clean_text = words.translate(str.maketrans('', '', string.punctuation))
        return clean_text
    
    def remove_stop_words(self, words: str):
        stop_word = set(stopwords.words('english'))
        words = word_tokenize(words)
        clean_text = [word for word in words if word.lower() not in stop_word]
        return clean_text
    
    def clean_all(self, words):
        clean_word = self.punctuation_cleaning(words=words)
        clean_word = self.remove_stop_words(clean_word)
        return " ".join(clean_word).lower()
    
