__author__ = 'wenjiezhong'

import csv
import os.path

pids = []
results_of_pid = []
unique_results_per_pid ={}

def get_file_path(filename):
    file_path = os.path.join(os.getcwd(), filename)
    return file_path

def read_csv(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            pids.append(row[0])
            results_of_pid.append(row[1])
path = get_file_path('Data/6.csv')
read_csv(path)

def write_counts_to_csv(file_name, count_list):
    writerentities_hashtagsDict = csv.writer(open(file_name, 'wb'))
    for key, value in sorted(count_list.items()):
       writerentities_hashtagsDict.writerow([key, value])

def process():
    i = 0
    while i < len(pids):
        j = 1
        temp_pid = pids[i]
        unique_results_per_pid[temp_pid] = 0
        while j < len(pids):
            if temp_pid == pids[j]:
                unique_results_per_pid[temp_pid] += int(results_of_pid[j])
            j += 1
        i += 1

process()
write_counts_to_csv('aggregated_results.csv', unique_results_per_pid)