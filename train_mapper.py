#!/usr/bin/env python
"""
Mapper reads in text documents and emits word counts by class.
INPUT:                                                    
    DocID \t true_class \t subject \t body                
OUTPUT:                                                   
    partitionKey \t word \t class0_partialCount,class1_partialCount       
    

Instructions:
    You know what this script should do, go for it!
    (As a favor to the graders, please comment your code clearly!)
    
    A few reminders:
    1) To make sure your results match ours please be sure
       to use the same tokenizing that we have provided in
       all the other jobs:
         words = re.findall(r'[a-z]+', text-to-tokenize.lower())
         
    2) Don't forget to handle the various "totals" that you need
       for your conditional probabilities and class priors.
       
Partitioning:
    In order to send the totals to each reducer, we need to implement
    a custom partitioning strategy.
    
    We will generate a list of keys based on the number of reduce tasks 
    that we read in from the environment configuration of our job.
    
    We'll prepend the partition key by hashing the word and selecting the
    appropriate key from our list. This will end up partitioning our data
    as if we'd used the word as the partition key - that's how it worked
    for the single reducer implementation. This is not necessarily "good",
    as our data could be very skewed. However, in practice, for this
    exercise it works well. The next step would be to generate a file of
    partition split points based on the distribution as we've seen in 
    previous exercises.
    
    Now that we have a list of partition keys, we can send the totals to 
    each reducer by prepending each of the keys to each total.
       
"""

import re                                                   
import sys                                                  
import numpy as np      

from operator import itemgetter
import os

#################### YOUR CODE HERE ###################
# initiate variable to read number of reducetasks from environment
N = int(os.getenv('mapreduce_job_reduces', default=1))

# create function to get hash of key based on number of reducers
def makeIndex(key, num_reducers = N):
    """
    key             the key that will be used for partitioning
    num_reducers    the number of reducers that will be configured
    """
    # for each character, get ascii
    byteof = lambda char: int(format(ord(char), 'b'), 2)
    current_hash = 0
    # get hash
    for c in key:
        current_hash = (current_hash * 31 + byteof(c))
    return current_hash % num_reducers

# function to get sorted partition keys based on hadoop sort of hashkeys
def makeKeyFile(num_reducers = N):
    KEYS = list(map(chr, range(ord('A'), ord('Z')+1)))[:num_reducers]
    partition_keys = sorted(KEYS, key=lambda k: makeIndex(k,num_reducers))
    return partition_keys


# store partitionkeys in a list
pKeys = makeKeyFile(N)


# initial variables
class0_doc_count=0
class1_doc_count=0
class0_word_count=0
class1_word_count=0
for line in sys.stdin:
    # parse input and tokenize
    docID, _class, subject, body = line.lower().split('\t')
    words = re.findall(r'[a-z]+', subject + ' ' + body)
    if _class == '1':
        # set partial counts for each class to emit for each word
        class0_partialCount,class1_partialCount = 0,1
        # increment doc count for class by 1
        class1_doc_count+=1
        # for each word, get partition keys
        for word in words:
            hashkey = makeIndex(word,N)
            key=pKeys[hashkey]
            #increment word count
            class1_word_count+=1
            #emit partition key, word, and partial counts
            print(f"{key}\t{word}\t{class0_partialCount},{class1_partialCount}")
    else:
        class0_partialCount,class1_partialCount = 1,0  
        class0_doc_count+=1
        for word in words:
            hashkey = makeIndex(word,N)
            key=pKeys[hashkey]
            class0_word_count+=1
            print(f"{key}\t{word}\t{class0_partialCount},{class1_partialCount}")
# for each ket, emit total_doc_count and total_ word_count for reducers
for key in pKeys:
    print(f"{key}\t{'*total_doc_count'}\t{class0_doc_count},{class1_doc_count}")
    print(f"{key}\t{'*total_word_count'}\t{class0_word_count},{class1_word_count}") 































#################### (END) YOUR CODE ###################