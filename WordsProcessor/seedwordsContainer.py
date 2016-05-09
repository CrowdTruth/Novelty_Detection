__author__ = 'wenjiezhong'

import csv
import os.path

#Input
seed_words = []
event_score = []
content = []

#Output
content_position = []

def write_counts_to_csv(file_name, list):
    writer = csv.writer(open(file_name, 'wb'))
    writer.writerow(list)

def get_file_path(filename):
    file_path = os.path.join(os.getcwd(), filename)
    return file_path

def read_csv(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            seed_words.append(row[0])

def read_csv_target(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            content.append(row[0])

path = get_file_path('Data/seedwords.csv')
read_csv(path)
path_target = get_file_path('Data/content.csv')
read_csv_target(path_target)

def process():
    i = 0
    while i < len(content):
        counter = 0
        words = content[i].split()
        for word in words:
            if word in seed_words:
                counter += 1
        if counter >= 2:
            content_position.append(1)
        else:
            content_position.append(0)
        i += 1

process()
write_counts_to_csv('content_position.txt', content_position)