__author__ = 'wenjiezhong'
import Metrics
import os
import csv

def get_file_path(filename):
    file_path = os.path.join(os.getcwd(), filename)
    return file_path

path_novel = get_file_path('data/CT_novelwords.csv')
path_NOTnovel = get_file_path('data/CT_NOTnovelwords.csv')
path_relevance = get_file_path('data/CT_Relevance.csv')
path_novelty = get_file_path('CT_NoveltyTweetSelection.csv')

#path_words = get_file_path('data/CT_word.csv')
worker = []
tweet = []
vector = []
workerdict = {}
worker_words = []
tweet_words = []
vector_words = []
workerdict_words = {}

def read_csv(filepath, worker, tweet, vector):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            worker.append(row[0])
            tweet.append(row [1])
            vector.append(row[2:])

try:
    read_csv(path_novel, worker, tweet, vector)
    print 'Novel words read succeeded'
except:
    pass
try:
    read_csv(path_NOTnovel, worker, tweet, vector)
    print 'NOTnovel words read succeeded'
except:
    pass
try:
    read_csv(path_relevance, worker, tweet, vector)
    print 'Relevance read succeeded'
except:
    pass
try:
    read_csv(path_novelty, worker, tweet, vector)
    print 'Novelty selection read succeeded'
except:
    pass
#read_csv(path_words, worker_words, tweet_words, vector_words)

def write_counts_to_csv(file_name, list):
    writer = csv.writer(open(file_name, 'wb'))
    for key, value in list.items():
        writer.writerow([key, value])

for i in range(0, len(vector)):
    vector[i] = list(map(int, vector[i]))

for i in range(0, len(vector_words)):
    vector_words[i] = list(map(int, vector_words[i]))

for x in range(0, len(worker)):
    if worker[x] in workerdict:
        current_worker_annotations = workerdict[worker[x]]
    else:
        current_worker_annotations = {}
    current_worker_annotations[tweet[x]] = vector[x]
    workerdict[worker[x]] = current_worker_annotations

for x in range(0, len(worker_words)):
    if worker_words[x] in workerdict_words:
        current_worker_annotations = workerdict_words[worker_words[x]]
    else:
        current_worker_annotations = {}
    current_worker_annotations[tweet_words[x]] = vector_words[x]
    workerdict_words[worker_words[x]] = current_worker_annotations

# workerdict[worker[x]] = {tweet[x]:vector[x]}
worker_agreement = Metrics.get_worker_agreement(workerdict)
cosine = Metrics.get_cosine_similarity(workerdict)

worker_unique = list(set(worker))

write_counts_to_csv('Novelty_Cosine.csv',cosine)
write_counts_to_csv('Novelty_Worker_Disagreement.csv',worker_agreement)