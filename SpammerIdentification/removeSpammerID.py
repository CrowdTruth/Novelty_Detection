__author__ = 'wenjiezhong'

import csv
import os.path
import itertools

#Input
worker_ID = []
spammer_list = []

#Output
clean_list = []
spammer_list_output = []

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
            spammer_list.append(row[12])

path = get_file_path('Data/aggregated_selections.csv')
read_csv(path)

i = 0
while i < len(worker_ID):
    if spammer_list[i][0] == '0':
        clean_list.append(worker_ID[i])
    else:
        spammer_list_output.append(worker_ID[i])
    i += 1

write_counts_to_csv('without_spammers.txt', clean_list)
write_counts_to_csv('spammers.txt', spammer_list_output)