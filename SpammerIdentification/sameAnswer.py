__author__ = 'wenjiezhong'
import csv
import os.path

#Input
worker_ID = []
more_novel = []
equally_novel = []
less_novel = []
irrelevant = []

#output
same_answer = []

def get_file_path(filename):
    file_path = os.path.join(os.getcwd(), filename)
    return file_path
def read_csv(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            worker_ID.append(row[0])
            more_novel.append(row[1])
            equally_novel.append(row[2])
            less_novel.append(row[3])
            irrelevant.append(row[4])
path = get_file_path('Data/aggregated_selections.csv')
read_csv(path)

def write_counts_to_csv(file_name, list):
    writer = csv.writer(open(file_name, 'wb'))
    writer.writerow(list)

def process():
    i = 0
    while i < len(worker_ID):
        #Always Irrelevant
        if more_novel[i] == '0' and equally_novel[i] == '0' and less_novel[i] == '0':
            same_answer.append(1)
        #Always less novel
        elif more_novel[i] == '0' and equally_novel[i] == '0' and irrelevant[i] == '0':
            same_answer.append(1)
        #Always equally novel
        elif more_novel[i] == '0' and less_novel[i] == '0' and irrelevant[i] == '0':
            same_answer.append(1)
        #Always more novel
        elif less_novel[i] == '0' and equally_novel[i] == '0' and irrelevant[i] == '0':
            same_answer.append(1)
        #Chose diversive
        else:
            same_answer.append(0)
        i += 1

process()
write_counts_to_csv('same_answer.txt', same_answer)