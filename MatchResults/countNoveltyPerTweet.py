__author__ = 'wenjiezhong'

import csv
import os.path

#Input
tweet_ID = []
more_novel = []
equally_novel = []
less_novel = []
irrelevant = []

presence_of_tweet_ID = []

#Output
counted_more_novel_per_tweet = {}
counted_equally_novel_per_tweet = {}
counted_less_novel_per_tweet = {}
counted_irrelevant_per_tweet = {}
counted_novelty_per_tweet = []

def write_counts_to_csv(file_name, list):
    writer = csv.writer(open(file_name, 'wb'))
    writer.writerow(list)

def get_file_path(filename):
    file_path = os.path.join(os.getcwd(), filename)
    return file_path

def read_csv(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            tweet_ID.append(row[1])
            more_novel.append(int(row[2]))
            equally_novel.append(int(row[3]))
            less_novel.append(int(row[4]))
            irrelevant.append(int(row[5]))

path = get_file_path('Data/clean_data.csv')
read_csv(path)

def prepopulate_tweets():
    for tweet in tweet_ID:
        counted_more_novel_per_tweet[tweet] = 0
        counted_equally_novel_per_tweet[tweet] = 0
        counted_less_novel_per_tweet[tweet] = 0
        counted_irrelevant_per_tweet[tweet] = 0

def process():
    i = 0
    while i < len(tweet_ID):
        j = i
        temp_tweet_ID = tweet_ID[i]
        while j < len(tweet_ID) and tweet_ID[i] not in presence_of_tweet_ID:
            if tweet_ID[j] == tweet_ID[i]:
                counted_more_novel_per_tweet[tweet_ID[i]] += more_novel[j]
                counted_equally_novel_per_tweet[tweet_ID[i]] += equally_novel[j]
                counted_less_novel_per_tweet[tweet_ID[i]] += less_novel[j]
                counted_irrelevant_per_tweet[tweet_ID[i]] += irrelevant[j]
            j += 1
        presence_of_tweet_ID.append(temp_tweet_ID)
        i += 1

def merge_novelty():
    for tweet in counted_more_novel_per_tweet:
        counted_novelty_per_tweet.append('%s,%s,%s,%s,%s' %(tweet,counted_more_novel_per_tweet[tweet],counted_equally_novel_per_tweet[tweet]
        ,counted_less_novel_per_tweet[tweet],counted_irrelevant_per_tweet[tweet]))

prepopulate_tweets()
process()
merge_novelty()
write_counts_to_csv('counted_novelty_per_tweet.txt', counted_novelty_per_tweet)