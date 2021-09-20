#!/usr/bin/env python
"""
Reducer to calculate precision and recall as part
of the inference phase of Naive Bayes.
INPUT:
    ID \t true_class \t P(ham|doc) \t P(spam|doc) \t predicted_class
OUTPUT:
    precision \t ##
    recall \t ##
    accuracy \t ##
    F-score \t ##
         
Instructions:
    Complete the missing code to compute these^ four
    evaluation measures for our classification task.
    
    Note: if you have no True Positives you will not 
    be able to compute the F1 score (and maybe not 
    precision/recall). Your code should handle this 
    case appropriately feel free to interpret the 
    "output format" above as a rough suggestion. It
    may be helpful to also print the counts for true
    positives, false positives, etc.
"""
import sys

# initialize counters
FP = 0.0 # false positives
FN = 0.0 # false negatives
TP = 0.0 # true positives
TN = 0.0 # true negatives

# read from STDIN
for line in sys.stdin:
    # parse input
    docID, class_, pHam, pSpam, pred = line.split()
    # emit classification results first
    print(line[:-2], class_ == pred)
    # then compute evaluation stats
#################### YOUR CODE HERE ###################
# if class is accurately predicted
    if class_== pred:
        # increment TP is class is 1 and TN if class is 0
        if class_=='1':
            TP+=1
        else:
            TN+=1
# if class is inaccurately predicted, increment FP and FN count
    else:
        if pred=='1':
            FP+=1
        else:
            FN+=1
# calculate metrics
accuracy= (TN+TP)/(TP+TN+FP+FN)
precision= TP/(TP+FP)
recall= TP/(TP+FN)
fscore= (2*precision*recall)/(precision+recall)
# emit report metrics
print(f"{'# Documents:'}\t{TP+FP+FN+TN}")
print(f"{'True Positives:'}\t{TP}")
print(f"{'True Negatives:'}\t{TN}")
print(f"{'False Positives:'}\t{FP}")
print(f"{'False Negatives:'}\t{FN}")
print(f"{'Accuracy:'}\t{accuracy}")
print(f"{'Precision:'}\t{precision}")
print(f"{'Recall:'}\t{recall}")
print(f"{'F-Score:'}\t{fscore}")























#################### (END) YOUR CODE ###################
    