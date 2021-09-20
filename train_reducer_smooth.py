#!/usr/bin/env python

import os
import sys                                                  
import numpy as np  

#################### YOUR CODE HERE ###################
class0_count=0
class1_count=0

current_word= None
for line in sys.stdin: 
    pkey, word, counts= line.split('\t')
    class0_partialCount,class1_partialCount= counts.split(',')
    class0_partialCount,class1_partialCount=float(class0_partialCount),float(class1_partialCount)
    if current_word is not None and word == current_word:
        class0_count += class0_partialCount
        class1_count += class1_partialCount
    else:
        # if word encountered in new non empty key then print word and count
        if current_word is not None:
            print ("{}\t{}\t{},{}".format(pkey,current_word,class0_count,class1_count))
            # key to store encounted word    
        current_word = word
        class0_count = float(class0_partialCount)
        class1_count = float(class1_partialCount)
print ("{}\t{}\t{},{}".format(pkey,current_word,class0_count,class1_count))      
































#################### (END) YOUR CODE ###################