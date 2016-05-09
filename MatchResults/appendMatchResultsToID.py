__author__ = 'wenjiezhong'

import csv
import os.path

pids_of_2015 = []
pids = []
results_of_pid = []
results_to_append = []

def get_file_path(filename):
    file_path = os.path.join(os.getcwd(), filename)
    return file_path

def read_csv(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            pids.append(row[0])
            results_of_pid.append(row[1])

with open('Data/2015.csv', 'rU') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        pids_of_2015.append(row[0])

path = get_file_path('Data/Complete.csv')
read_csv(path)

def write_counts_to_csv(file_name, count_list):
    writer = csv.writer(open(file_name, 'wb'))
    writer.writerow(count_list)

def process():
    i = 0
    while i < len(pids_of_2015):
        j = 0
        boolean_appended = False
        while j < len(pids):
            if pids_of_2015[i] == pids[j]:
                results_to_append.append(results_of_pid[j])
                boolean_appended = True
            elif boolean_appended == False and j == len(pids)-1:
                results_to_append.append('null')
            j += 1
        i += 1

process()
write_counts_to_csv('appended_results.txt', results_to_append)