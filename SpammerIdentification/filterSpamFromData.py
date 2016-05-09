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
spammers = []

#Output
clean_data = []

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
            worker_ID.append(row[0])
            tweet_ID.append(row[1])
            more_novel.append(row[2])
            equally_novel.append(row[3])
            less_novel.append(row[4])
            irrelevant.append(row[5])

def read_csv_spammers(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            spammers.append(row[0])

path = get_file_path('Data/CT_NoveltyTweetSelection.csv')
path_spammers = get_file_path('Data/spammers.csv')
read_csv(path)
read_csv_spammers(path_spammers)

def process():
    i = 0
    clean_data.append('worker_ID,tweet_ID,more_novel,equally_novel,less_novel,NA')
    while i < len(worker_ID):
        if worker_ID[i] not in spammers:
            clean_data.append('%s,%s,%s,%s,%s,%s' %(worker_ID[i],tweet_ID[i],more_novel[i],equally_novel[i],less_novel[i],irrelevant[i]))
        i += 1

process()
write_counts_to_csv('clean_data.txt', clean_data)