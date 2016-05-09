__author__ = 'wenjiezhong'

import csv
import os.path

#Input
line_of_words_irrelevant = []
not_novel_value_irrelevant = []
line_of_words_NOT = []
not_novel_value_NOT = []
line_of_words_novel = []
not_novel_value_novel = []
worker_irrelevant = []
worker_NOT = []
worker_novel = []
tweet_irrelevant = []
tweet_NOT = []
tweet_novel = []

pre_line_of_words_NOT = []
pre_line_of_words_novel = []

header_novel = ['worker_ID', 'tweet_ID', 'word0', 'word1', 'word2', 'word3', 'word4', 'word5', 'word6', 'word7', 'word8', 'word9', 'word10', 'word11', 'word12', 'word13', 'word14', 'word15', 'word16', 'word17', 'word18', 'word19', 'word20', 'word21', 'word22', 'word23', 'word24', 'word25', 'word26', 'word27', 'NONE', 'check_failed']
header_NOT = ['worker_ID', 'tweet_ID', 'word0', 'word1', 'word2', 'word3', 'word4', 'word5', 'word6', 'word7', 'word8', 'word9', 'word10', 'word11', 'word12', 'word13', 'word14', 'word15', 'word16', 'word17', 'word18', 'word19', 'word20', 'word21', 'word22', 'word23', 'word24', 'word25', 'word26', 'word27', 'NONE']
empty_words = '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'
#Output
novel_list = []
not_novel_list = []

def get_file_path(filename):
    file_path = os.path.join(os.getcwd(), filename)
    return file_path

def read_csv_irrelevant(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            worker_irrelevant.append(row[0])
            tweet_irrelevant.append(row[1])
            line_of_words_irrelevant.append(row[2:30])
            not_novel_value_irrelevant.append(row[30])

def read_csv_NOTnovel(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            worker_NOT.append(row[0])
            tweet_NOT.append(row[1])
            pre_line_of_words_NOT.append(row[2:30])
            not_novel_value_NOT.append(row[30])

def read_csv_novel(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            worker_novel.append(row[0])
            tweet_novel.append(row[1])
            pre_line_of_words_novel.append(row[2:30])
            not_novel_value_novel.append(row[30])

path_irrelevant = get_file_path('Data/CT_Irrelevantwords.csv')
path_NOTnovel = get_file_path('Data/CT_NOTnovelwords.csv')
path_novel = get_file_path('Data/CT_novelwords.csv')
read_csv_irrelevant(path_irrelevant)
read_csv_NOTnovel(path_NOTnovel)
read_csv_novel(path_novel)

tweet_irrelevant = [tweet_irrelevant.strip(' ') for tweet_irrelevant in tweet_irrelevant]
tweet_NOT = [tweet_NOT.strip(' ') for tweet_NOT in tweet_NOT]
tweet_novel = [tweet_novel.strip(' ') for tweet_novel in tweet_novel]

def prestuff():
    for line in pre_line_of_words_novel:
        precursor_novel = ",".join(line)
        precursor_novel = precursor_novel.replace(" ", "")
        line_of_words_novel.append(precursor_novel)
    for line in pre_line_of_words_NOT:
        precursor_NOT = ",".join(line)
        precursor_NOT = precursor_NOT.replace(" ", "")
        line_of_words_NOT.append(precursor_NOT)

def write_counts_to_csv(file_name, count_list):
    writer = csv.writer(open(file_name, 'wb'))
    writer.writerow(count_list)

def process_novel_list():
    novel_list.append(", ".join(header_novel))
    i = 0
    while i < len(worker_irrelevant):
        novel_list.append('%s,%s,%s,1,0' %(worker_irrelevant[i],tweet_irrelevant[i],empty_words))
        i += 1
    j = 0
    while j < len(worker_NOT):
        if '1' in line_of_words_NOT[j]:
            novel_list.append('%s,%s,%s,0,0' %(worker_NOT[j],tweet_NOT[j],line_of_words_NOT[j]))
        else:
            novel_list.append('%s,%s,%s,1,0' %(worker_NOT[j],tweet_NOT[j],line_of_words_NOT[j]))
        j += 1
    k = 0
    while k < len(worker_novel):
        if '1' in line_of_words_novel[k]:
            novel_list.append('%s,%s,%s,0,0' %(worker_novel[k],tweet_novel[k],line_of_words_novel[k]))
        else:
            novel_list.append('%s,%s,%s,0,1' %(worker_novel[k],tweet_novel[k],line_of_words_novel[k]))
        k += 1

def process_NOTnovel_list():
    not_novel_list.append(", ".join(header_NOT))
    i = 0
    while i < len(worker_irrelevant):
        not_novel_list.append('%s,%s,%s,1' %(worker_irrelevant[i],tweet_irrelevant[i],empty_words))
        i += 1
    j = 0
    while j < len(worker_NOT):
        if '1' in line_of_words_NOT[j]:
            not_novel_list.append('%s,%s,%s,0' %(worker_NOT[j],tweet_NOT[j],line_of_words_NOT[j]))
        else:
            not_novel_list.append('%s,%s,%s,1' %(worker_NOT[j],tweet_NOT[j],line_of_words_NOT[j]))
        j += 1
    k = 0
    while k < len(worker_novel):
        if '1' in line_of_words_novel[k]:
            not_novel_list.append('%s,%s,%s,0' %(worker_novel[k],tweet_novel[k],line_of_words_novel[k]))
        else:
            not_novel_list.append('%s,%s,%s,1' %(worker_novel[k],tweet_novel[k],line_of_words_novel[k]))
        k += 1

prestuff()
process_novel_list()
process_NOTnovel_list()
write_counts_to_csv('CT_novelwords.txt', novel_list)
write_counts_to_csv('CT_NOTnovelwords.txt', not_novel_list)