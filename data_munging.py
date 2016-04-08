import pandas as pd
import numpy as np
import scipy as sp
import csv 
import itertools
ids = []
seqs = []

with open('chicken_train.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    i = 0
    for row in spamreader:
        #print row
        i = i+1
        #if i == 5:
        #    break
        buff = row[0].split(',')
        ids.append(buff[0])
        seqs.append(buff[1])


#print len(ids),ids[0:3]
#print len(seqs), seqs[0:3]


print "Generate histogram"

k = 3
alphabet = ['a', 'c', 'g', 't']
combin = []
for i in itertools.product(['a','c','g','t'], repeat=k):
    combin.append(str(i[0],i[1],i[2]))

print combin[0:30]
freq = [0]*len(combin)

#for subs in combin:
