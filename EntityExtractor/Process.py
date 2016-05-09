__author__ = 'marc'

from Extractors import TextRazorApi, NerdApi, SpotLightApi
from collections import Counter
from nltk.corpus import sentiwordnet as swn
import json
import codecs
import csv
from pymongo import MongoClient


def process():
    i = 1
    with codecs.open('Data/tweets.txt', encoding='utf8') as f:
        lines = f.readlines()
        for text in lines:
            print "(%s) >>> %s" % (i, text)

            entities = TextRazorApi.process_textrazor_api(text)
            entities += NerdApi.process_nerd_api(text)
            entities += SpotLightApi.process_spotlight_api(text)

            write_to_mongo("localhost", 27017, "Tweets", "whaling_nlp", entities)
            i += 1


def get_labels_from_mongo():
    client = MongoClient('localhost', 27017)
    db = client.Tweets
    entities = db.whaling_nlp.find({},{'label': 1})
    return [entity['label'] for entity in entities]


def count_labels_and_add_sentiment_score(labels):
    counts = Counter(labels).most_common()

    sentiment_list = []
    sentiment_list.append(['label', 'count', 'positive', 'negative'])
    for label, count in counts:
        synsets = swn.senti_synsets(label)
        if len(synsets) == 0:
            positive = 0.0
            negative = 0.0
        else:
            t = synsets[0]
            positive = t.pos_score()
            negative = t.neg_score()

        sentiment_list.append(
            [
                label.encode("ASCII", 'ignore'),
                count,
                positive,
                negative
            ]
        )

    return sentiment_list


def write_counts_to_csv(file_name, count_list):
    with open(file_name, 'wb') as out:
        wr = csv.writer(out)
        for keyword in count_list:
            wr.writerow(keyword)


def write_to_mongo(server, port, db, collection, documents):
    """ Store in MongoDB
    Write string in json format to MongoDB Database

    :param server: MongoDB server (i.e. localhost)
    :param port: MongoDB port (i.e. 27017)
    :param db: MongoDB database name (i.e. activist_events)
    :param collection: MongoDB collection name (i.e. whaling_evenst)
    :param document: json string to write to the DB
    :return: document is stored in the database
    """
    client = MongoClient(server, port)
    db = client[db]
    collection = db[collection]
    for document in documents:
        document = json.dumps(document)
        collection.insert(json.loads(document))


###########################
#    Starting Point
###########################
process()
labels = get_labels_from_mongo()
sentiment_list = count_labels_and_add_sentiment_score(labels)
write_counts_to_csv('counts.csv', sentiment_list)
