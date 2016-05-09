__author__ = 'wenjiezhong'

import csv
import os.path
import itertools

#Input
tweet_ID_source = []
tweet_content = []
date = []

tweet_ID_target = []

#Output
output_tweet_data = []

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
            tweet_ID_source.append(row[0])
            tweet_content.append(row[1])
            date.append(row[2])

def read_csv_target(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            tweet_ID_target.append(row[0])

path = get_file_path('Data/content.csv')
path_tweets = get_file_path('Data/counted_novelty_per_tweet.csv')
read_csv(path)
read_csv_target(path_tweets)

def process():
    i = 0
    while i < len(tweet_ID_target):
        j = tweet_ID_source.index(tweet_ID_target[i])
        output_tweet_data.append('%s,%s' %(tweet_content[j],date[j]))
        i += 1

process()
write_counts_to_csv('output_tweet_data.txt', output_tweet_data)
