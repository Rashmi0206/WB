#!/usr/bin/env python
"""
Reducer aggregates word counts by class and emits frequencies.

INPUT:
    partitionKey \t word \t class0_partialCount,class1_partialCount
OUTPUT:
    word \t class0_count,class1_count,pclass0,pclass1 
    
Instructions:
    Again, you are free to design a solution however you see 
    fit as long as your final model meets our required format
    for the inference job we designed in Question 8. Please
    comment your code clearly and concisely.
    
    A few reminders: 
    1) Don't forget to emit Class Priors (with the right key).
    2) In python2: 3/4 = 0 and 3/float(4) = 0.75
"""
##################### YOUR CODE HERE ####################
import sys
#initializing variables to 0
total_class0_Count=0
total_class1_Count=0
total_word_class0Count=0
total_word_class1Count=0
class0_count=0
class1_count=0
#setting current word
current_word= None
#reading each line from standard input
for line in sys.stdin: 
    #spliting line by tab to get partitionkey, word and counts tuple
    pkey, word, counts= line.split('\t')
    #spliting counts tuple to get class0 and class1 partialcounts
    class0_partialCount,class1_partialCount= counts.split(',')
    #convert  to float
    class0_partialCount,class1_partialCount=float(class0_partialCount),float(class1_partialCount)
    # to increment counts for word that is repeatedly encountered
    if current_word is not None and word == current_word:
        class0_count += class0_partialCount
        class1_count += class1_partialCount
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
            else:
                pclass0= class0_count/total_word_class0Count
                pclass1= class1_count/total_word_class1Count
                print ("{}\t{},{},{},{}".format(current_word,class0_count,class1_count,pclass0,pclass1))
        # set current word and counts   
        current_word = word
        class0_count = float(class0_partialCount)
        class1_count = float(class1_partialCount)
#edge case to handle if partition only has totals but no words
if not current_word == '*total_word_count':
    pclass0= class0_count/total_word_class0Count
    pclass1= class1_count/total_word_class1Count
    print ("{}\t{},{},{},{}".format(current_word,class0_count,class1_count,pclass0,pclass1))      

        






























##################### (END) CODE HERE ####################