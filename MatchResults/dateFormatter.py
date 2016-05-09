__author__ = 'wenjiezhong'

import csv
import os.path
import datetime

dates = []
formatted_dates = []

def get_file_path(filename):
    file_path = os.path.join(os.getcwd(), filename)
    return file_path

def read_csv(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            dates.append(row[0])
path = get_file_path('Data/date.csv')
read_csv(path)

def write_to_csv(file_name, list):
    writer = csv.writer(open(file_name, 'wb'))
    writer.writerow(list)

def process():
    for date in dates:
        formatted_dates.append(datetime.datetime.strptime(date, '%a %b %d %H:%M:%S %Y').strftime('%d-%m %H:%M:%S'))

process()
write_to_csv('formatted_dates.txt', formatted_dates)