import nltk 
from nltk.sentiment.vader import SentimentIntensityAnalyzer 

class AnalyticsService:
    def sotrted_common_words(self, words: list):
        my_dict = {}
        for word in words:
            if word in my_dict:
                my_dict[word] += 1
                continue
            my_dict[word] = 1  
        return sorted(my_dict.items(), key=lambda x: x[1], reverse=True)  
    
    def get_10_commend_words(self, words: list):
        words_list = []
        if len(words) > 10:
             for word in words:
                words_list.append(word[0])
             return words_list[:10]
        for word in words:
                words_list.append(word[0])
        return words_list
    
    def sort_and_get_10(self, words: str):
        data = words.split()
        data = self.sotrted_common_words(data)
        data = self.get_10_commend_words(data)
        return data
    
    def read_file_woopen(self):
        wepone_list = []
        with open('data/weapon_list.txt') as f:
            for line in f:
                wepone_list.append(line.strip())  
        return wepone_list
    
    def search_for_weapons(self, data: list):
        wepone_list = self.read_file_woopen()
        wepone_in_data = []
        for word in data:
            if (word in wepone_list) and (word not in wepone_in_data):
                wepone_in_data.append(word)
        return wepone_list     
       
    def get_sentiment(self, text: str):
        nltk.download('vader_lexicon')# Compute sentiment labels 
        Score = SentimentIntensityAnalyzer().polarity_scores(text)
        return Score

    def check_sentiment(self, sentiment: dict):
        if sentiment['compound'] > 0.5000 and sentiment['compound'] <= 1.000:
            return 'POSITIVE'
        if sentiment['compound'] < 0.4999 and sentiment['compound'] > -0.4991:
            return 'NEUTRAL'
        return 'NEGATIVE'
    
    def do_all(self, data: dict):
        data['10_commend_words'] = self.sort_and_get_10(data['clean_words'])
        data['weapons'] = self.search_for_weapons(data['clean_words'].split())
        data['sentiment_clean_words'] = self.check_sentiment(self.get_sentiment(data['clean_words']))
        data['sentiment'] = self.check_sentiment(self.get_sentiment(data['words']))
        return data

