__author__ = 'wenjiezhong'

import csv
import os.path

description = []
retrieved_length =[]

def get_file_path(filename):
    file_path = os.path.join(os.getcwd(), filename)
    return file_path

def read_csv(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            description.append(row[0])
path = get_file_path('Data/description.csv')
read_csv(path)

def write_counts_to_csv(file_name, count_list):
    with open(file_name, 'wb') as out:
        wr = csv.writer(out)
        wr.writerow(count_list)

def process():
    for sentence in description:
        if sentence is not None:
            retrieved_length.append(len(sentence))
        else:
            retrieved_length.append(len(0))

process()
write_counts_to_csv('length_of_description.csv', retrieved_length)