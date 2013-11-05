#!/usr/bin/env python -tt

import random
import numpy as np
import Levenshtein as lev
import sys


def process(word, bernoulli_p):
    new_word = ""
    for letter in word:
        failed_trial = np.random.geometric(p=bernoulli_p)-1
        if failed_trial:
            choice = random.randint(97, 132)
            if 128 <= choice <= 132:
                letter = ""
            elif 123 <= choice <= 127:
                letter = letter + chr(random.randint(97, 122))
            else:
                letter = chr(choice)
        new_word += letter
    return new_word


def mean_dissimilarity(string, the_list):
    num_comps = 0
    running_sum = 0
    for item in the_list:
        running_sum += lev.distance(string, item)
        num_comps += 1
    return float(running_sum)/float(num_comps)

def get_winner(lstrings):
    ltuples = []
    for item in lstrings:
        the_mean = mean_dissimilarity(item, lstrings)
        ltuples.append((the_mean, item))
    return sorted(ltuples)[0][1]

def mutate_string(string, num_times, prob):
    lstrings = []
    for i in xrange(0, num_times):
        lstrings.append(process(string, prob))
    return lstrings

def percent_correct(string, mut_strings):
    num_correct = 0
    length = len(mut_strings)
    for item in mut_strings:
        if item == string:
            num_correct += 1
    return float(num_correct)/float(length)

def perform_trial(string, num_mutations, b_prob):
    strings = mutate_string(string, num_mutations, b_prob)
    perc_correct = percent_correct(string, strings)
    winner = get_winner(strings)
    if winner == string:
        return (perc_correct, True)
    return (perc_correct, False)

def success_rate(string, num_mutations, b_prob, reps):
    successes = 0
    percs_correct = []
    for i in xrange(0, reps):
        trial_results = perform_trial(string, num_mutations, b_prob)
        percs_correct.append(trial_results[0])
        if trial_results[1]:
            successes += 1
    mean_perc_correct = float(sum(percs_correct))/float(len(percs_correct))
    perc_succ = float(successes)/float(reps)
    #print "{}\t{}".format(str(mean_perc_correct), str(perc_succ))
    return (str(mean_perc_correct), str(perc_succ))



def debug(string, num_mutations, b_prob):
    strings = mutate_string(string, num_mutations, b_prob)
    ltuples = []
    for item in strings:
        the_mean = mean_dissimilarity(item, strings)
        print str(the_mean) + "\t" + item
        ltuples.append((the_mean, item))
    print "Winner!: {}".format(sorted(ltuples)[0][1])
    return sorted(ltuples)[0][1]



# for word in ["morrissey", "counterrevolutionaries"]:
#     for sample in [5, 20, 100]:
#         for i in [.99, .98, .95, .9, .85, .8, .75, .7]:
#             rate = success_rate(word, sample, i, 1000)
#             print "{}\t{}\t{}\t{}\t{}". format(word, str(sample), str(i), 
#                                          rate[0], rate[1])
#             sys.stdout.flush()


# for word in ["morrissey"]:
#     for sample in xrange(1, 51):
#         #for i in [.99, .98, .95, .9, .85, .8, .75, .7]:
#         for i in [.80]:
#             rate = success_rate(word, sample, i, 1000)
#             print "{}\t{}\t{}\t{}\t{}". format(word, str(sample), str(i), 
#                                          rate[0], rate[1])
#             sys.stdout.flush()


"""
print ".99"
success_rate(word, 5, .99, 1000)
print ".98"
success_rate(word, 5, .98, 1000)
print ".95"
success_rate(word, 5, .95, 1000)
print ".9"
success_rate(word, 5, .9, 1000)
print ".85"
success_rate(word, 5, .85, 1000)
print ".8"
success_rate(word, 5, .8, 1000)
print ".75"
success_rate(word, 5, .75, 1000)
print ".7"
success_rate(word, 5, .7, 1000)
"""
