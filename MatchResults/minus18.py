__author__ = 'wenjiezhong'

import csv
import os.path

ev_a = [[117 for x in range(1)] for x in range(9)]
ev_b = [[117 for x in range(1)] for x in range(9)]

def get_file_path(filename):
    file_path = os.path.join(os.getcwd(), filename)
    return file_path

def read_csv(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            ev_a[0].append(row[5])
            ev_b[0].append(row[6])
            ev_a[1].append(row[7])
            ev_b[1].append(row[8])
            ev_a[2].append(row[9])
            ev_b[2].append(row[10])
            ev_a[3].append(row[11])
            ev_b[3].append(row[12])
            ev_a[4].append(row[13])
            ev_b[4].append(row[14])
            ev_a[5].append(row[15])
            ev_b[5].append(row[16])
            ev_a[6].append(row[17])
            ev_b[6].append(row[18])
            ev_a[7].append(row[19])
            ev_b[7].append(row[20])
            ev_a[8].append(row[21])
            ev_b[8].append(row[22])
path = get_file_path('Data/f764698.csv')
read_csv(path)

def write_counts_to_csv(file_name, list):
    writer = csv.writer(open(file_name, 'wb'))
    writer.writerows(list)

def process():
    i = 0
    j = 0
    while i < len(ev_a[0]):
        while j < len(ev_a):
            if ev_a[j][i] and ev_a[j][i] != 'NA':
                ev_a[j][i] = str(int(ev_a[j][i]) - 18)
            j += 1
        i += 1
        j = 0
    i = 0
    while i < len(ev_a[0]):
        while j < len(ev_a):
            if ev_b[j][i] and ev_b[j][i] != 'NA':
                ev_b[j][i] = str(int(ev_b[j][i]) - 18)
            j += 1
        i += 1
        j = 0

process()
write_counts_to_csv('minus_18A.csv', ev_a)
write_counts_to_csv('minus_18B.csv', ev_b)