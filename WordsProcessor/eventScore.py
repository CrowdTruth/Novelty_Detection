__author__ = 'wenjiezhong'

import csv
import os.path

#Input
tweet_ID = []
event_score = []
tweet_ID_target = []

#Output
event_score_position = []

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
            tweet_ID.append(row[0])
            event_score.append(float(row[1]))

def read_csv_target(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            tweet_ID_target.append(row[0])

path = get_file_path('Data/tweeteventscore.csv')
read_csv(path)
path_target = get_file_path('Data/target.csv')
read_csv_target(path_target)

def process():
    i = 0
    while i < len(tweet_ID_target):
        j = tweet_ID.index(tweet_ID_target[i])
        event_score_position.append(event_score[j])
        i += 1

process()
write_counts_to_csv('event_score_position.txt', event_score_position)