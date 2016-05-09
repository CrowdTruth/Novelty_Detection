__author__ = 'wenjiezhong'

import codecs
import csv
import os.path

retrieved_entities = []
calculated_entities_per_tweet = []

def get_file_path(filename):
    file_path = os.path.join(os.getcwd(), filename)
    return file_path

def read_csv(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            retrieved_entities.append(row[0])
path = get_file_path('Data/counts.csv')
read_csv(path)

def process():
    counted_entities_per_tweet = 0
    with codecs.open('Data/tweets.txt', encoding='utf8') as f:
        lines = f.readlines()
        for text in lines:
            tweet_words_separated = text.split()
            for word in tweet_words_separated:
                if any(word in s for s in retrieved_entities):
                    counted_entities_per_tweet += 1
            calculated_entities_per_tweet.append(counted_entities_per_tweet)
            counted_entities_per_tweet = 0

def write_counts_to_csv(file_name, count_list):
    with open(file_name, 'wb') as out:
        wr = csv.writer(out)
        wr.writerow(count_list)

process()
write_counts_to_csv('counted_entities.csv', calculated_entities_per_tweet)

