#!/usr/bin/env python
"""
INPUT: 
    {pkey}\t{current_word}\t{class0_count},{class1_count}           
OUTPUT:                                                   
    {pkey}\t{current_word}\t{class0_count},{class1_count}             
"""

import re                                                   
import sys                                                  
import numpy as np      

from operator import itemgetter
import os

#################### YOUR CODE HERE ###################
N = int(os.getenv('mapreduce_job_reduces', default=1))

def makeIndex(key, num_reducers = N):
    """
    key             the key that will be used for partitioning
    num_reducers    the number of reducers that will be configured
    """
    byteof = lambda char: int(format(ord(char), 'b'), 2)
    current_hash = 0
    for c in key:
        current_hash = (current_hash * 31 + byteof(c))
    return current_hash % num_reducers

def makeKeyFile(num_reducers = N):
    KEYS = list(map(chr, range(ord('A'), ord('Z')+1)))[:num_reducers]
    partition_keys = sorted(KEYS, key=lambda k: makeIndex(k,num_reducers))
    return partition_keys

# call your helper function to get partition keys for vocab count
pKeys = makeKeyFile(N)

#counter for vocabulary size
vocab_count=0
for line in sys.stdin:
    pkey, word, counts= line.strip('\n').split('\t')
    if not word[0]=='*':
        vocab_count+=1
    print(f"{pkey}\t{word}\t{counts}") 
# to emit vocab count to all partitions
for key in pKeys:
    print(f"{key}\t{'*vocab_count'}\t{vocab_count},{vocab_count}")
































#################### (END) YOUR CODE ###################