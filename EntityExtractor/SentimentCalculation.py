__author__ = 'wenjiezhong'

from nltk.corpus import sentiwordnet as swn
import codecs
import csv
import os.path

tweets = []
calculated_sentiment_per_tweet =[]

def get_file_path(filename):
    file_path = os.path.join(os.getcwd(), filename)
    return file_path

def read_csv(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            tweets.append(row[0])
path = get_file_path('Data/tweets.txt')
read_csv(path)

def process():
    counted_sentiment_per_tweet = 0
    with codecs.open('Data/tweets.txt', encoding='utf8') as f:
        lines = f.readlines()
        for text in lines:
            tweet_words_separated = text.split()
            for word in tweet_words_separated:
                try:
                    if any(word.decode('utf-8') in s for s in tweets):
                        synsets = swn.senti_synsets(word.decode('utf-8'))
                        if len(synsets) == 0:
                            positive = 0.0
                            negative = 0.0
                        else:
                            t = synsets[0]
                            positive = t.pos_score()
                            negative = t.neg_score()
                            counted_sentiment_per_tweet += positive - negative
                except:
                    print ''
            calculated_sentiment_per_tweet.append(counted_sentiment_per_tweet)
            print counted_sentiment_per_tweet
            counted_sentiment_per_tweet = 0

def write_counts_to_csv(file_name, count_list):
    with open(file_name, 'wb') as out:
        wr = csv.writer(out)
        wr.writerow(count_list)

process()
write_counts_to_csv('calculated_entities.csv', calculated_sentiment_per_tweet)


