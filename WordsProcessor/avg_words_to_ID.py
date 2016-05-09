__author__ = 'wenjiezhong'

import csv
import os.path

#Input
worker_ID = []
worker_ID_to_process = []
worker_ID_to_processNOT = []
words_avg = []
words_avgNOT = []

#Output
avg_words_position = []
avg_words_positionNOT = []

def get_file_path(filename):
    file_path = os.path.join(os.getcwd(), filename)
    return file_path

def read_csv(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            worker_ID.append(row[0])

def read_csvWorker(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            worker_ID_to_process.append(row[0])
            words_avg.append(float(row[1]))

def read_csvWorkerNOT(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            worker_ID_to_processNOT.append(row[0])
            words_avgNOT.append(float(row[1]))

path = get_file_path('Data/aggregated_selections.csv')
read_csv(path)
path_workerIDs = get_file_path('Data/avg_novel_words.csv')
path_workerIDsNOT = get_file_path('Data/avg_NOT_novel_words.csv')
read_csvWorker(path_workerIDs)
read_csvWorkerNOT(path_workerIDsNOT)

def write_counts_to_csv(file_name, list):
    writer = csv.writer(open(file_name, 'wb'))
    writer.writerow(list)

def process():
    i = 0
    while i < len(worker_ID):
        j = 0
        boolean_index = False
        while j < len(worker_ID_to_process):
            if worker_ID[i] == worker_ID_to_process[j]:
                avg_words_position.append("{0:.2f}".format(round(words_avg[j],2)))
                boolean_index = True
            elif j == len(worker_ID_to_process)-1 and boolean_index == False:
                avg_words_position.append('NONE')
            j += 1
        i += 1

def processNOT():
    i = 0
    while i < len(worker_ID):
        j = 0
        boolean_index = False
        while j < len(worker_ID_to_processNOT):
            if worker_ID[i] == worker_ID_to_processNOT[j]:
                avg_words_positionNOT.append("{0:.2f}".format(round(words_avgNOT[j],2)))
                boolean_index = True
            elif j == len(worker_ID_to_processNOT)-1 and boolean_index == False:
                avg_words_positionNOT.append('NONE')
            j += 1
        i += 1

process()
processNOT()
write_counts_to_csv('avg_words_index.txt', avg_words_position)
write_counts_to_csv('avg_words_index_NOT.txt', avg_words_positionNOT)