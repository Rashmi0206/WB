#!/usr/bin/env python

import os
import sys                                                  
import numpy as np  

#################### YOUR CODE HERE ###################
total_class0_Count=0
total_class1_Count=0
total_word_class0Count=0
total_word_class1Count=0
class0_count=0
class1_count=0
vocab_Count=0
current_word= None
for line in sys.stdin: 
    pkey, word, counts= line.split('\t')
    class0_partialCount,class1_partialCount= counts.split(',')
    class0_partialCount,class1_partialCount=float(class0_partialCount),float(class1_partialCount)
    if current_word is not None and word == current_word and current_word== '*vocab_count':
        class0_count += class0_partialCount
        class1_count += class1_partialCount
    elif current_word is not None and word == current_word:
        class0_count = class0_partialCount
        class1_count = class1_partialCount
    else:
        # if word encountered in new non empty key then print word and count
        if current_word is not None:
            if current_word == '*total_doc_count':
                total_class0_Count = class0_count
                total_class1_Count = class1_count
                class0_prior = total_class0_Count/(total_class0_Count+total_class1_Count)
                class1_prior = total_class1_Count/(total_class0_Count+total_class1_Count)
                if pkey=='A':
                    print(f"ClassPriors\t{total_class0_Count},{total_class1_Count},{class0_prior},{class1_prior}")
            elif current_word == '*total_word_count':
                total_word_class0Count =class0_count
                total_word_class1Count =class1_count
            elif current_word == '*vocab_count':
                vocab_Count =class0_count
            else:
                pclass0= (class0_count+1)/(total_word_class0Count+vocab_Count)
                pclass1= (class1_count+1)/(total_word_class1Count+vocab_Count)
                print ("{}\t{},{},{},{}".format(current_word,class0_count,class1_count,pclass0,pclass1))
                # key to store encounted word    
        current_word = word
        class0_count = float(class0_partialCount)
        class1_count = float(class1_partialCount)
if not current_word == '*vocab_count':
    pclass0= (class0_count+1)/(total_word_class0Count+vocab_Count)
    pclass1= (class1_count+1)/(total_word_class1Count+vocab_Count)
    print ("{}\t{},{},{},{}".format(current_word,class0_count,class1_count,pclass0,pclass1))      
     
































#################### (END) YOUR CODE ###################