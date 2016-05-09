__author__ = 'wenjiezhong'

import csv
import os.path
import urllib2
from urlparse import urlparse

urls1 = []
urls2 = []
base_urls1 =[]
base_urls2 =[]

def get_file_path(filename):
    file_path = os.path.join(os.getcwd(), filename)
    return file_path

def read_csv(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            urls1.append(row[0])
            urls2.append(row[1])
path = get_file_path('Data/urls.csv')
read_csv(path)

def write_counts_to_csv(file_name, count_list):
    with open(file_name, 'wb') as out:
        wr = csv.writer(out)
        wr.writerow(count_list)

def process():
    i = 0
    for sentence in urls1:
        if sentence:
            try:
                unshortened_url = urllib2.urlopen(sentence)
                parsed_uri = urlparse(unshortened_url.url)
                base_urls1.append('{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri))
            except:
                base_urls1.append('NOT FOUND')
        else:
            base_urls1.append('null')
        i += 1
        print i
    for sentence in urls2:
        if sentence:
            try:
                unshortened_url = urllib2.urlopen(sentence)
                parsed_uri = urlparse(unshortened_url.url)
                base_urls2.append('{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri))
            except:
                base_urls2.append('NOT FOUND')
        else:
            base_urls2.append('null')



process()
write_counts_to_csv('base_urls1.csv', base_urls1)
write_counts_to_csv('base_urls2.csv', base_urls2)

