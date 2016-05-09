__author__ = 'wenjiezhong'

import csv
import os.path

#Input
worker_ID = []
more_novel = []
equally_novel = []
less_novel = []
irrelevant = []

#Output
irrelevant_behaviour_score = []

def get_file_path(filename):
    file_path = os.path.join(os.getcwd(), filename)
    return file_path

def read_csv(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            worker_ID.append(row[0])
            more_novel.append(float(row[1]))
            equally_novel.append(float(row[2]))
            less_novel.append(float(row[3]))
            irrelevant.append(float(row[4]))

path = get_file_path('Data/aggregated_selections.csv')
read_csv(path)

def write_counts_to_csv(file_name, list):
    writer = csv.writer(open(file_name, 'wb'))
    writer.writerow(list)

def process():
    i = 0
    while i < len(worker_ID):
        total_temp = more_novel[i] + equally_novel[i] + less_novel[i] + irrelevant[i]
        irrelevant_behaviour_score.append(irrelevant[i]/total_temp)
        i += 1

process()
write_counts_to_csv('irrelevant_behaviour.txt', irrelevant_behaviour_score)