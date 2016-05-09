__author__ = 'wenjiezhong'

import csv
import os.path

#Input
worker_ID = []
tweet_ID = []
more_novel = []
equally_novel = []
less_novel = []
irrelevant = []

weight = 0.5

#Intermediate Variables
tweet_ID_dict = {}
count_of_tweets = {}
presence_of_tweet_ID = []

#Output
tweet_ID_dict_output = {}

def write_counts_to_csv(file_name, list):
    writer = csv.writer(open(file_name, 'wb'))
    for key, value in list.items():
        writer.writerow([key, value])

def get_file_path(filename):
    file_path = os.path.join(os.getcwd(), filename)
    return file_path

def read_csv(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            worker_ID.append(row[0])
            tweet_ID.append(row[1])
            more_novel.append(row[2])
            equally_novel.append(row[3])
            less_novel.append(row[4])
            irrelevant.append(row[5])

path = get_file_path('Data/clean_data.csv')
read_csv(path)

def prepopulate_tweets():
    for tweet in tweet_ID:
        tweet_ID_dict[tweet] = 0
        count_of_tweets[tweet] = 0

def process():
    i = 0
    while i < len(worker_ID):
        j = i
        temp_tweet_ID = tweet_ID[i]
        while j < len(worker_ID) and tweet_ID[i] not in presence_of_tweet_ID:
            if tweet_ID[j] == temp_tweet_ID:
                if more_novel[j][0] == '1':
                    tweet_ID_dict[tweet_ID[i]] += 1
                    count_of_tweets[tweet_ID[i]] += 1
                elif equally_novel[j][0] == '1':
                    tweet_ID_dict[tweet_ID[i]] += weight
                    count_of_tweets[tweet_ID[i]] += 1
                elif less_novel[j][0] == '1':
                    tweet_ID_dict[tweet_ID[i]] -= 1
                    count_of_tweets[tweet_ID[i]] += 1
                else:
                    count_of_tweets[tweet_ID[i]] += 1
            j += 1
        presence_of_tweet_ID.append(temp_tweet_ID)
        i += 1

def merge_counts_and_sum():
    for tweet in tweet_ID:
        tweet_ID_dict_output[tweet] = '%s,%s,%s' %(count_of_tweets[tweet],tweet_ID_dict[tweet],float(tweet_ID_dict[tweet])/max(tweet_ID_dict.values()))

prepopulate_tweets()
process()
merge_counts_and_sum()
write_counts_to_csv('counted_scores.txt', tweet_ID_dict_output)