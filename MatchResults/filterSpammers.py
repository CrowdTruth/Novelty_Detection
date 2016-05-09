__author__ = 'wenjiezhong'

import csv
import os.path
import numpy as np

worker_ID = []
CT_Agreements = []
worker_Agreements_Dict = {}
worker_as_spammer = {}

def write_counts_to_csv(file_name, list):
    writer = csv.writer(open(file_name, 'wb'))
    for key, value in list.items():
        writer.writerow([key, value])

def get_file_path(filename):
    file_path = os.path.join(os.getcwd(), filename)
    return file_path

def read_csv(filepath, worker_ID, CT_Agreements):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            worker_ID.append(row[0])
            CT_Agreements.append(float(row[1]))

#Match Results
path = get_file_path('Data/Match_results.csv')
read_csv(path, worker_ID, CT_Agreements)

j = 0
for i in CT_Agreements:
    worker_Agreements_Dict[worker_ID[j]] = CT_Agreements[j]
    j += 1

st_dev = np.std(CT_Agreements)
mean = np.mean(CT_Agreements)
threshold = mean - st_dev

for i in worker_Agreements_Dict:
    if worker_Agreements_Dict[i] < threshold:
        worker_as_spammer[i] = worker_Agreements_Dict[i]

#Word Results
worker_ID_words = []
CT_Agreements_words = []
worker_Agreements_Dict_words = {}
worker_as_spammer_words = {}

path_words = get_file_path('Data/Word_count.csv')
read_csv(path_words, worker_ID_words, CT_Agreements_words)

k = 0
for i in CT_Agreements:
    worker_Agreements_Dict_words[worker_ID_words[k]] = CT_Agreements_words[k]
    k += 1

st_dev_words = np.std(CT_Agreements_words)
mean_words = np.mean(CT_Agreements_words)
threshold_words = mean_words - st_dev_words

for i in worker_Agreements_Dict_words:
    if worker_Agreements_Dict_words[i] < threshold_words:
        worker_as_spammer_words[i] = worker_Agreements_Dict_words[i]

write_counts_to_csv('filt_spam_competition.csv', worker_as_spammer)
write_counts_to_csv('filt_spam_words.csv', worker_as_spammer_words)