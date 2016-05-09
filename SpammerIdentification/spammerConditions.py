__author__ = 'wenjiezhong'

import csv
import os.path
import numpy as np

#Input
worker_cosine_1 = {}
worker_disagreement_2 = {}
worker_consistency_3 = []
consistency_value_3 = []
worker_irrelevant_behaviour_4 = {}
worker_annotation_frequency_5 = {}
avg_novelty_selected = {}
avg_novel_words = {}
more_novel = {}
equally_novel = {}
less_novel = {}
irrelevant = {}

worker_consistency_dict_3 = {}
worker_ID_list = []

#Output
spammer = []
explanation_1_2 = []
explanation_1or2_3or4or5 = []
explanation_4_5 = []
avg_irrelevant_threshold = []
avg_novel_selection = []
explanation_output = []

#Consistency 3
def get_file_path_3(filename):
    file_path = os.path.join(os.getcwd(), filename)
    return file_path
def read_csv_3(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            worker_consistency_3.append(row[0])
            consistency_value_3.append(float(row[5]))
path_3 = get_file_path_3('Data/Consistency.csv')
read_csv_3(path_3)

#Irrelevant Behaviour 4 and worker annotation frequency 5
#avg_irrelevant_selected and avg_novelty_selected
def get_file_path_4(filename):
    file_path = os.path.join(os.getcwd(), filename)
    return file_path
def read_csv_4(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            key = row[0]
            worker_irrelevant_behaviour_4[key] = float(row[5])
            worker_ID_list.append(row[0])
            avg_novelty_selected[key] = float(row[6])
            worker_annotation_frequency_5[key] = row[7]
            worker_cosine_1[key] = float(row[10])
            worker_disagreement_2[key] = float(row[11])
            try:
                avg_novel_words[key] = float(row[8])
            except:
                avg_novel_words[key] = 0
            more_novel[key] = float(row[1])
            equally_novel[key] = float(row[2])
            less_novel[key] = float(row[3])
            irrelevant[key] = float(row[4])
path_4 = get_file_path_4('Data/aggregated_selections.csv')
read_csv_4(path_4)

def write_counts_to_csv(file_name, list):
    writer = csv.writer(open(file_name, 'wb'))
    writer.writerow(list)

def mean_std_dev_COS():
    total_cos = 0.0
    list_cos = []
    for worker in worker_cosine_1:
        total_cos += worker_cosine_1[worker]
        list_cos.append(float(worker_cosine_1[worker]))
    mean_cos = total_cos/len(worker_cosine_1)
    std_dev_cos = np.std(list_cos)
    threshold_cos = mean_cos - std_dev_cos
    return threshold_cos

def mean_std_dev_DIS():
    total_dis = 0.0
    list_dis = []
    for worker in worker_disagreement_2:
        total_dis += worker_disagreement_2[worker]
        list_dis.append(float(worker_disagreement_2[worker]))
    mean_cos = total_dis/len(worker_disagreement_2)
    std_dev_dis = np.std(list_dis)
    threshold_dis = mean_cos - std_dev_dis
    return threshold_dis

def mean_std_dev_COS2():
    total_cos = 0.0
    list_cos = []
    for worker in worker_cosine_1:
        total_cos += worker_cosine_1[worker]
        list_cos.append(float(worker_cosine_1[worker]))
    mean_cos = total_cos/len(worker_cosine_1)
    std_dev_cos = np.std(list_cos)
    threshold_cos = mean_cos - std_dev_cos - std_dev_cos
    return threshold_cos

def mean_std_dev_DIS2():
    total_dis = 0.0
    list_dis = []
    for worker in worker_disagreement_2:
        total_dis += worker_disagreement_2[worker]
        list_dis.append(float(worker_disagreement_2[worker]))
    mean_cos = total_dis/len(worker_disagreement_2)
    std_dev_dis = np.std(list_dis)
    threshold_dis = mean_cos - std_dev_dis - std_dev_dis
    return threshold_dis

def mean_half_std_dev_COS():
    total_cos = 0.0
    list_cos = []
    for worker in worker_cosine_1:
        total_cos += worker_cosine_1[worker]
        list_cos.append(float(worker_cosine_1[worker]))
    mean_cos = total_cos/len(worker_cosine_1)
    std_dev_cos = np.std(list_cos)
    threshold_cos = mean_cos - (1.25 * std_dev_cos)
    return threshold_cos

def mean_half_std_dev_DIS():
    total_dis = 0.0
    list_dis = []
    for worker in worker_disagreement_2:
        total_dis += worker_disagreement_2[worker]
        list_dis.append(float(worker_disagreement_2[worker]))
    mean_cos = total_dis/len(worker_disagreement_2)
    std_dev_dis = np.std(list_dis)
    threshold_dis = mean_cos - (0.75 * std_dev_dis)
    return threshold_dis

def aggregate_consistency():
    j = 0
    for worker in worker_consistency_3:
        worker_consistency_dict_3[worker] = 0
        j += 1
    i = 0
    for worker in worker_consistency_3:
        worker_consistency_dict_3[worker] += consistency_value_3[i]
        i += 1

def processV1():
    threshold_cos = mean_std_dev_COS()
    threshold_dis = mean_std_dev_DIS()
    print threshold_cos
    print threshold_dis
    i = 0
    while i < len(worker_ID_list):
        if worker_cosine_1[worker_ID_list[i]] < threshold_cos and worker_disagreement_2[worker_ID_list[i]] < threshold_dis:
            spammer.append(1)
            explanation_1_2.append(1)
            explanation_1or2_3or4or5.append(0)
            explanation_4_5.append(0)
            avg_irrelevant_threshold.append(0)
            avg_novel_selection.append(0)
        elif worker_cosine_1[worker_ID_list[i]] < threshold_cos or worker_disagreement_2[worker_ID_list[i]] < threshold_dis:
            if worker_consistency_dict_3[worker_ID_list[i]] == '1' or worker_irrelevant_behaviour_4[worker_ID_list[i]] > 0.5 or worker_annotation_frequency_5[worker_ID_list[i]] == '1':
                spammer.append(1)
                explanation_1_2.append(0)
                explanation_1or2_3or4or5.append(1)
                explanation_4_5.append(0)
                avg_irrelevant_threshold.append(0)
                avg_novel_selection.append(0)
            else:
                spammer.append(0)
                explanation_1_2.append(0)
                explanation_1or2_3or4or5.append(0)
                explanation_4_5.append(0)
                avg_irrelevant_threshold.append(0)
                avg_novel_selection.append(0)
        elif worker_irrelevant_behaviour_4[worker_ID_list[i]] > 0.5 and worker_annotation_frequency_5[worker_ID_list[i]] == '1':
            spammer.append(1)
            explanation_1_2.append(0)
            explanation_1or2_3or4or5.append(0)
            explanation_4_5.append(1)
            avg_irrelevant_threshold.append(0)
            avg_novel_selection.append(0)
        elif worker_irrelevant_behaviour_4[worker_ID_list[i]] > 0.5:
            spammer.append(1)
            explanation_1_2.append(0)
            explanation_1or2_3or4or5.append(0)
            explanation_4_5.append(0)
            avg_irrelevant_threshold.append(1)
            avg_novel_selection.append(0)
        elif avg_novelty_selected[worker_ID_list[i]] > 0.75:
            spammer.append(1)
            explanation_1_2.append(0)
            explanation_1or2_3or4or5.append(0)
            explanation_4_5.append(0)
            avg_irrelevant_threshold.append(0)
            avg_novel_selection.append(1)
        else:
            spammer.append(0)
            explanation_1_2.append(0)
            explanation_1or2_3or4or5.append(0)
            explanation_4_5.append(0)
            avg_irrelevant_threshold.append(0)
            avg_novel_selection.append(0)
        i += 1
    create_explanation1()

def processV2():
    threshold_cos = mean_std_dev_COS()
    threshold_dis = mean_std_dev_DIS()
    i = 0
    while i < len(worker_ID_list):
        if worker_cosine_1[worker_ID_list[i]] < threshold_cos and worker_disagreement_2[worker_ID_list[i]] < threshold_dis:
            spammer.append(1)
            explanation_1_2.append(1)
            explanation_1or2_3or4or5.append(0)
            explanation_4_5.append(0)
            avg_irrelevant_threshold.append(0)
            avg_novel_selection.append(0)
        elif worker_cosine_1[worker_ID_list[i]] < threshold_cos or worker_disagreement_2[worker_ID_list[i]] < threshold_dis:
            if worker_consistency_dict_3[worker_ID_list[i]] == '1' or worker_irrelevant_behaviour_4[worker_ID_list[i]] > 0.5 or worker_annotation_frequency_5[worker_ID_list[i]] == '1':
                spammer.append(1)
                explanation_1_2.append(0)
                explanation_1or2_3or4or5.append(1)
                explanation_4_5.append(0)
                avg_irrelevant_threshold.append(0)
                avg_novel_selection.append(0)
            else:
                spammer.append(0)
                explanation_1_2.append(0)
                explanation_1or2_3or4or5.append(0)
                explanation_4_5.append(0)
                avg_irrelevant_threshold.append(0)
                avg_novel_selection.append(0)
        elif worker_irrelevant_behaviour_4[worker_ID_list[i]] > 0.5 and worker_annotation_frequency_5[worker_ID_list[i]] == '1':
            spammer.append(1)
            explanation_1_2.append(0)
            explanation_1or2_3or4or5.append(0)
            explanation_4_5.append(1)
            avg_irrelevant_threshold.append(0)
            avg_novel_selection.append(0)
        elif worker_irrelevant_behaviour_4[worker_ID_list[i]] > 0.5 and avg_novelty_selected[worker_ID_list[i]] > 0.75:
            spammer.append(1)
            explanation_1_2.append(0)
            explanation_1or2_3or4or5.append(0)
            explanation_4_5.append(0)
            avg_irrelevant_threshold.append(1)
            avg_novel_selection.append(0)
        else:
            spammer.append(0)
            explanation_1_2.append(0)
            explanation_1or2_3or4or5.append(0)
            explanation_4_5.append(0)
            avg_irrelevant_threshold.append(0)
            avg_novel_selection.append(0)
        i += 1
    create_explanation2()

def processV3():
    threshold_cos = mean_std_dev_COS()
    threshold_dis = mean_std_dev_DIS()
    i = 0
    while i < len(worker_ID_list):
        if worker_cosine_1[worker_ID_list[i]] < threshold_cos and worker_disagreement_2[worker_ID_list[i]] < threshold_dis:
            spammer.append(1)
            explanation_1_2.append(1)
            explanation_1or2_3or4or5.append(0)
            explanation_4_5.append(0)
            avg_irrelevant_threshold.append(0)
            avg_novel_selection.append(0)
        elif worker_cosine_1[worker_ID_list[i]] < threshold_cos or worker_disagreement_2[worker_ID_list[i]] < threshold_dis:
            if worker_consistency_dict_3[worker_ID_list[i]] == '1' or worker_irrelevant_behaviour_4[worker_ID_list[i]] > 0.5 or worker_annotation_frequency_5[worker_ID_list[i]] == '1':
                spammer.append(1)
                explanation_1_2.append(0)
                explanation_1or2_3or4or5.append(1)
                explanation_4_5.append(0)
                avg_irrelevant_threshold.append(0)
                avg_novel_selection.append(0)
            else:
                spammer.append(0)
                explanation_1_2.append(0)
                explanation_1or2_3or4or5.append(0)
                explanation_4_5.append(0)
                avg_irrelevant_threshold.append(0)
                avg_novel_selection.append(0)
        elif worker_irrelevant_behaviour_4[worker_ID_list[i]] > 0.5 and worker_annotation_frequency_5[worker_ID_list[i]] == '1':
            spammer.append(1)
            explanation_1_2.append(0)
            explanation_1or2_3or4or5.append(0)
            explanation_4_5.append(1)
            avg_irrelevant_threshold.append(0)
            avg_novel_selection.append(0)
        elif worker_irrelevant_behaviour_4[worker_ID_list[i]] > 0.5 and avg_novelty_selected[worker_ID_list[i]] > 0.75:
            spammer.append(1)
            explanation_1_2.append(0)
            explanation_1or2_3or4or5.append(0)
            explanation_4_5.append(0)
            avg_irrelevant_threshold.append(1)
            avg_novel_selection.append(0)
        elif worker_annotation_frequency_5[worker_ID_list[i]] == '1':
            spammer.append(1)
            explanation_1_2.append(0)
            explanation_1or2_3or4or5.append(0)
            explanation_4_5.append(0)
            avg_irrelevant_threshold.append(0)
            avg_novel_selection.append(1)
        else:
            spammer.append(0)
            explanation_1_2.append(0)
            explanation_1or2_3or4or5.append(0)
            explanation_4_5.append(0)
            avg_irrelevant_threshold.append(0)
            avg_novel_selection.append(0)
        i += 1
    create_explanation1()

def processV4():
    threshold_cos = mean_std_dev_COS2()
    threshold_dis = mean_std_dev_DIS2()
    i = 0
    while i < len(worker_ID_list):
        if worker_cosine_1[worker_ID_list[i]] < threshold_cos and worker_disagreement_2[worker_ID_list[i]] < threshold_dis:
            spammer.append(1)
            explanation_1_2.append(1)
            explanation_1or2_3or4or5.append(0)
            explanation_4_5.append(0)
            avg_irrelevant_threshold.append(0)
            avg_novel_selection.append(0)
        elif worker_cosine_1[worker_ID_list[i]] < threshold_cos or worker_disagreement_2[worker_ID_list[i]] < threshold_dis:
            if worker_consistency_dict_3[worker_ID_list[i]] == '1' or worker_irrelevant_behaviour_4[worker_ID_list[i]] > 0.5 or worker_annotation_frequency_5[worker_ID_list[i]] == '1':
                spammer.append(1)
                explanation_1_2.append(0)
                explanation_1or2_3or4or5.append(1)
                explanation_4_5.append(0)
                avg_irrelevant_threshold.append(0)
                avg_novel_selection.append(0)
            else:
                spammer.append(0)
                explanation_1_2.append(0)
                explanation_1or2_3or4or5.append(0)
                explanation_4_5.append(0)
                avg_irrelevant_threshold.append(0)
                avg_novel_selection.append(0)
        elif worker_irrelevant_behaviour_4[worker_ID_list[i]] > 0.5 and worker_annotation_frequency_5[worker_ID_list[i]] == '1':
            spammer.append(1)
            explanation_1_2.append(0)
            explanation_1or2_3or4or5.append(0)
            explanation_4_5.append(1)
            avg_irrelevant_threshold.append(0)
            avg_novel_selection.append(0)
        elif worker_irrelevant_behaviour_4[worker_ID_list[i]] > 0.5 and avg_novelty_selected[worker_ID_list[i]] > 0.75:
            spammer.append(1)
            explanation_1_2.append(0)
            explanation_1or2_3or4or5.append(0)
            explanation_4_5.append(0)
            avg_irrelevant_threshold.append(1)
            avg_novel_selection.append(0)
        else:
            spammer.append(0)
            explanation_1_2.append(0)
            explanation_1or2_3or4or5.append(0)
            explanation_4_5.append(0)
            avg_irrelevant_threshold.append(0)
            avg_novel_selection.append(0)
        i += 1
    create_explanation2()

def processV6():
    threshold_cos = mean_half_std_dev_COS()
    threshold_dis = mean_half_std_dev_DIS()
    print threshold_cos
    print threshold_dis
    i = 0
    while i < len(worker_ID_list):
        if worker_cosine_1[worker_ID_list[i]] < threshold_cos and worker_disagreement_2[worker_ID_list[i]] < threshold_dis:
            spammer.append(1)
            explanation_1_2.append(1)
            explanation_1or2_3or4or5.append(0)
            explanation_4_5.append(0)
            avg_irrelevant_threshold.append(0)
            avg_novel_selection.append(0)
        elif worker_cosine_1[worker_ID_list[i]] < threshold_cos or worker_disagreement_2[worker_ID_list[i]] < threshold_dis:
            if worker_consistency_dict_3[worker_ID_list[i]] == '1' or worker_irrelevant_behaviour_4[worker_ID_list[i]] > 0.5 \
                    or worker_annotation_frequency_5[worker_ID_list[i]] == '1' or avg_novel_words[worker_ID_list[i]] < 2:
                spammer.append(1)
                explanation_1_2.append(0)
                explanation_1or2_3or4or5.append(1)
                explanation_4_5.append(0)
                avg_irrelevant_threshold.append(0)
                avg_novel_selection.append(0)
            else:
                spammer.append(0)
                explanation_1_2.append(0)
                explanation_1or2_3or4or5.append(0)
                explanation_4_5.append(0)
                avg_irrelevant_threshold.append(0)
                avg_novel_selection.append(0)
        elif worker_irrelevant_behaviour_4[worker_ID_list[i]] > 0.5 and worker_annotation_frequency_5[worker_ID_list[i]] == '1':
            spammer.append(1)
            explanation_1_2.append(0)
            explanation_1or2_3or4or5.append(0)
            explanation_4_5.append(1)
            avg_irrelevant_threshold.append(0)
            avg_novel_selection.append(0)
        elif worker_annotation_frequency_5[worker_ID_list[i]] == '1' and avg_novel_words[worker_ID_list[i]] < 1.2 and \
            (more_novel[worker_ID_list[i]]+equally_novel[worker_ID_list[i]]+less_novel[worker_ID_list[i]]+irrelevant[worker_ID_list[i]]) > 7:
            spammer.append(1)
            explanation_1_2.append(0)
            explanation_1or2_3or4or5.append(0)
            explanation_4_5.append(0)
            avg_irrelevant_threshold.append(0)
            avg_novel_selection.append(1)
        else:
            spammer.append(0)
            explanation_1_2.append(0)
            explanation_1or2_3or4or5.append(0)
            explanation_4_5.append(0)
            avg_irrelevant_threshold.append(0)
            avg_novel_selection.append(0)
        i += 1
    create_explanation1()

def create_explanation1():
    i = 0
    explanation_output.append('1and2,1or2_3or4or5,4and5,avg_irr50,avg_nov75')
    while i < len(spammer):
        explanation_output.append('%s,%s,%s,%s,%s' %(explanation_1_2[i],explanation_1or2_3or4or5[i]
                                                   ,explanation_4_5[i],avg_irrelevant_threshold[i]
                                                   ,avg_novel_selection[i]))
        i += 1

def create_explanation2():
    i = 0
    explanation_output.append('1and2,1or2_3or4or5,4and5,avg_irr50')
    while i < len(spammer):
        explanation_output.append('%s,%s,%s,%s' %(explanation_1_2[i],explanation_1or2_3or4or5[i]
                                                   ,explanation_4_5[i],avg_irrelevant_threshold[i]))
        i += 1

aggregate_consistency()
processV6()

write_counts_to_csv('spammer.txt', spammer)
write_counts_to_csv('explanation.txt', explanation_output)