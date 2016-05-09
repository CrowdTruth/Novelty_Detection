__author__ = 'wenjiezhong'

import csv
import os.path

#Input
worker_ID = []
worker_IDSelection = []
more_novel = []
equally_novel = []
nowords_highlighted = []
irrelevant = []

#Output
worker_aggregated_choices = {}
worker_aggregated_choices_toWrite = {}
more_novelOutput = {}
equally_novelOutput = {}
nowords_highlightedOutput = {}
irrelevantOutput = {}

output_worker_aggregated = []

def get_file_path(filename):
    file_path = os.path.join(os.getcwd(), filename)
    return file_path

def read_csv(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            worker_IDSelection.append(row[0])
            more_novel.append(int(row[2]))
            equally_novel.append(int(row[3]))
            nowords_highlighted.append(int(row[4]))
            irrelevant.append(int(row[5]))

def read_csvWorker(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        #next(reader)
        for row in reader:
            worker_ID.append(row[0])

path = get_file_path('Data/CT_NoveltyTweetSelection.csv')
read_csv(path)
path_workerIDs = get_file_path('Data/Match_results.csv')
read_csvWorker(path_workerIDs)

def write_counts_to_csv(file_name, count_list):
    writer = csv.writer(open(file_name, 'wb'))
    writer.writerow(count_list)

def prepopulate_workerIDs():
    for worker in worker_ID:
        more_novelOutput[worker] = 0
        equally_novelOutput[worker] = 0
        nowords_highlightedOutput[worker] = 0
        irrelevantOutput[worker] = 0

def process():
    for worker in worker_ID:
        i = 0
        while i < len(more_novel):
            if worker_IDSelection[i] == worker:
                more_novelOutput[worker] += more_novel[i]
                equally_novelOutput[worker] += equally_novel[i]
                nowords_highlightedOutput[worker] += nowords_highlighted[i]
                irrelevantOutput[worker] += irrelevant[i]
            i += 1

def create_aggregate_dict():
    output_worker_aggregated.append('worker_ID,more_novel,equally_novel,less_novel,irrelevant')
    for worker in worker_ID:
        output_worker_aggregated.append('%s,%s,%s,%s,%s' %(worker,more_novelOutput[worker],equally_novelOutput[worker],nowords_highlightedOutput[worker],irrelevantOutput[worker]))

prepopulate_workerIDs()
process()
create_aggregate_dict()
write_counts_to_csv('aggregated_selections.txt', output_worker_aggregated)