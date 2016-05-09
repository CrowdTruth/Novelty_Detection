__author__ = 'wenjiezhong'

import csv
import os.path

#Input
worker_ID = []
more_novel = []
equally_novel = []
less_novel = []
header = ['worker_ID', 'tweet_ID', 'word0', 'word1', 'word2', 'word3', 'word4', 'word5', 'word6', 'word7', 'word8', 'word9', 'word10', 'word11', 'word12', 'word13', 'word14', 'word15', 'word16', 'word17', 'word18', 'word19', 'word20', 'word21', 'word22', 'word23', 'word24', 'word25', 'word26', 'word27', 'not_novel', 'check_failed']

#Output
novel_list = []
not_novel_list = []
irrelevant_list = []

def get_file_path(filename):
    file_path = os.path.join(os.getcwd(), filename)
    return file_path

def read_csv(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        novel_list.append(", ".join(header))
        not_novel_list.append(", ".join(header))
        irrelevant_list.append(", ".join(header))
        next(reader)
        for row in reader:
            worker_ID.append(row[0:32])
            more_novel.append(row[32])
            equally_novel.append(row[33])
            less_novel.append(row[34])

path = get_file_path('Data/ToSplitWords.csv')
read_csv(path)

def write_counts_to_csv(file_name, count_list):
    writer = csv.writer(open(file_name, 'wb'))
    writer.writerow(count_list)

def process():
    i = 0
    while i < len(more_novel):
        if more_novel[i] == '1' or equally_novel[i] == '1':
            novel_list.append(", ".join(worker_ID[i]))
        elif less_novel[i] == '1':
            not_novel_list.append(", ".join(worker_ID[i]))
        else:
            irrelevant_list.append(", ".join(worker_ID[i]))
        i += 1

process()
write_counts_to_csv('CT_novelwords.txt', novel_list)
write_counts_to_csv('CT_NOTnovelwords.txt', not_novel_list)
write_counts_to_csv('CT_Irrelevantwords.txt', irrelevant_list)