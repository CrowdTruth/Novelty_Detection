__author__ = 'wenjiezhong'

import csv
import os.path
import itertools

#Input
tweet_ID_source = []
tweet_content = {}
date = []

tweet_ID_target = []

#Output
output_tweet_data = {}

def write_counts_to_csv(file_name, dict):
    writer = csv.writer(open(file_name, 'wb'))
    for key, value in dict.items():
        writer.writerow([key, value])

def get_file_path(filename):
    file_path = os.path.join(os.getcwd(), filename)
    return file_path

def read_csv(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            key = row[0]
            tweet_content[key] = row[1:]

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
    for worker_ID in tweet_content:
        if worker_ID in tweet_ID_target:
            output_tweet_data[worker_ID] = tweet_content[worker_ID]

process()
write_counts_to_csv('output_tweet_data.txt', output_tweet_data)
