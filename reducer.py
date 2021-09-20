#!/usr/bin/env python
"""
Reducer takes words with their class and partial counts and computes totals.
INPUT:
    word \t class \t partialCount 
OUTPUT:
    word \t class \t totalCount  
"""
import re
import sys

# initialize trackers
current_word = None
spam_count, ham_count = 0,0

# read from standard input
for line in sys.stdin:
    # parse input
    word, is_spam, count = line.split('\t')
    
############ YOUR CODE HERE #########
    # check if the word is same as current_word
    if word == current_word: 
        # check if the class is spam
        # since the input for class is string, we have to compare with string
        if is_spam == '1':
            #increment spam count
            spam_count += int(count)
        else:
            #increment ham count
            ham_count += int(count)
        # OR emit current total and start a new tally 
    else: 
        if current_word:
            print(f'{current_word}\t{1}\t{spam_count}')
            print(f'{current_word}\t{0}\t{ham_count}')
        if is_spam == '1':
            current_word,spam_count,ham_count = word,int(count),0
        else:
            current_word,spam_count,ham_count = word,0,int(count)

 # don't forget the last record! 
print(f'{current_word}\t{1}\t{spam_count}')
print(f'{current_word}\t{0}\t{ham_count}')














############ (END) YOUR CODE #########