__author__ = 'wenjiezhong'

import csv
import os.path

#Input
worker_ID = []
words_listNOT = []
worker_ID_to_process = []
worker_ID_to_processNOT = []
words_list = []

#Output
avg_words_per_worker = {}
avg_words_per_worker_output = {}
avg_words_per_workerNOT = {}
avg_words_per_worker_outputNOT = {}

def get_file_path(filename):
    file_path = os.path.join(os.getcwd(), filename)
    return file_path

def read_csv(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            worker_ID_to_process.append(row[0])
            words_list.append(row[2:29])

def read_csvNOT(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            worker_ID_to_processNOT.append(row[0])
            words_listNOT.append(row[2:29])

def read_csvWorker(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            worker_ID.append(row[0])

path = get_file_path('Data/CT_novelwords.csv')
pathNOT = get_file_path('Data/CT_NOTnovelwords.csv')
read_csv(path)
read_csvNOT(pathNOT)
path_workerIDs = get_file_path('Data/Match_results.csv')
read_csvWorker(path_workerIDs)

def write_counts_to_csv(file_name, list):
    writer = csv.writer(open(file_name, 'wb'))
    for key, value in list.items():
        writer.writerow([key, value])

def prepopulate_workerIDs():
    for worker in worker_ID:
        avg_words_per_worker[worker] = 0
        avg_words_per_workerNOT[worker] = 0

def process():
    for worker in worker_ID:
        i = 0
        count_worker = 0
        while i < len(worker_ID_to_process):
            if worker_ID_to_process[i] == worker:
                avg_words_per_worker[worker] += sum(map(float, words_list[i]))
                count_worker += 1
                avg_words_per_worker_output[worker] = avg_words_per_worker[worker]/count_worker
            i += 1

def processNOT():
    for worker in worker_ID:
        i = 0
        count_worker = 0
        while i < len(worker_ID_to_processNOT):
            if worker_ID_to_processNOT[i] == worker:
                avg_words_per_workerNOT[worker] += sum(map(float, words_listNOT[i]))
                count_worker += 1
                avg_words_per_worker_outputNOT[worker] = avg_words_per_workerNOT[worker]/count_worker
            i += 1

prepopulate_workerIDs()
process()
processNOT()
write_counts_to_csv('avg_novel_words.csv', avg_words_per_worker_output)
write_counts_to_csv('avg_NOT_novel_words.csv', avg_words_per_worker_outputNOT)