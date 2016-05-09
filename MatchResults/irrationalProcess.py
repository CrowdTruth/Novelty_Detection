__author__ = 'wenjiezhong'

import csv
import os.path

more_novel = []
equally_novel = []
nowords_highlighted = []
irrational_worker = []

def get_file_path(filename):
    file_path = os.path.join(os.getcwd(), filename)
    return file_path

def read_csv(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            more_novel.append(row[2])
            equally_novel.append(row[3])
            nowords_highlighted.append(row[4])

path = get_file_path('Data/Irrational.csv')
read_csv(path)

def write_counts_to_csv(file_name, count_list):
    writer = csv.writer(open(file_name, 'wb'))
    writer.writerow(count_list)

def process():
    i = 0
    while i < len(more_novel):
        if equally_novel[i] == '1' and nowords_highlighted[i] == '1':
            irrational_worker.append(1)
        elif more_novel[i] == '1' and nowords_highlighted[i] == '1':
            irrational_worker.append(1)
        else:
            irrational_worker.append(0)
        i += 1

process()
write_counts_to_csv('irrational.txt', irrational_worker)