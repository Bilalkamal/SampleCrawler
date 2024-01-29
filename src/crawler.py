# crawler.py

import datetime
from bs4 import BeautifulSoup
from newspaper import Article
from extruct import extract
import nltk
from nltk.tokenize import sent_tokenize
import readtime
from textblob import TextBlob

class Crawler:
    def __init__(self, url):
        self.url = url
        self.article = None
        self.soup = None
        self.data = {}
        nltk.download('punkt', quiet=True)
    
    def get_data(self):
        return self.data


    def crawl(self):
        self.article = Article(self.url)
        self.article.download()
        self.article.parse()
        self.soup = BeautifulSoup(self.article.html, 'html.parser')



    def collect_data(self):
        
        self.data['title'] = self.article.title
        self.data['text'] = self.article.text
        self.data['authors'] = self.article.authors
        self.data['publish_date'] = datetime.datetime.strftime(self.article.publish_date, '%Y-%m-%d %H:%M:%S') if self.article.publish_date else None
        
        # json-ld, microformats, RDFa, etc.
        self.data['structured_data'] = extract(self.article.html, base_url=self.url)
        self.data['text_length'] = len(self.article.text)
        self.data['avg_sent_length'] = self.get_avg_sent_length()
        self.data['word_count'] = self.get_word_count()
        self.data['paragraph_count'] = self.get_paragraph_count()
        self.data['reading_time'] = self.get_reading_time().text
        self.data['sentiment'] = self.get_sentiment()

        
    def get_avg_sent_length(self):
        sentences = sent_tokenize(self.article.text)
        sentence_lengths = [len(sentence.split()) for sentence in sentences]
        return  sum(sentence_lengths) / len(sentence_lengths)

    def get_word_count(self):
        word_count = len(self.article.text.split())
        return word_count

    def get_paragraph_count(self):
        return self.article.text.count('\n')

    def get_reading_time(self):
        return readtime.of_text(self.article.text)

    def get_sentiment(self):
        return TextBlob(self.article.text).sentiment
