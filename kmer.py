import csv
import itertools
import numpy as np
import pickle

print "Generate all k-mer sequences"

alphabets = ['a','c','g','t']
N = 3
keywords = [''.join(i) for i in itertools.product(alphabets, repeat = N)]
#print keywords[0:631]
hist = {}
for i in keywords:
    #print i
    hist[i] = 0
X = np.zeros([64,631])
Y = np.zeros([631])

#print X[63,429]

linenum = 0
#print hist['aaa'], hist['aat']
with open("FLU_Challenge_HA_chicken.csv", "rb") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        for i in keywords:
            hist[i] = 0

        #print linenum
        id = row["ID"]
        if id == '':
            id = 2
            #print "-----"
            #break
        Y[linenum] = int(id)
        seq = str(row["seqs"])
        n_mer = []
        x=0

        #hist = []* (4**N)
        while x < len(seq)-N+1:
            #print seq[x-N:x]
            n_mer.append(seq[x: x+N])
            #n_mer.sort()
            x = x+1
            #print n_mer


    #Loop through the n_mer
        for word in n_mer:
            #print hist[str(word)]
            if word in hist.keys():
                hist[word] = hist[word] + 1
        for i in range(4**N) :
            #print keywords[i]
            X[i, linenum] = hist[keywords[i]]

        linenum += 1
        if linenum == 631:
            break



#print 'Y', Y
#print 'X', X

X_in = X[:, np.where(Y != 2)]
X_in = X_in[:,0,:]
Y_in = Y[np.where(Y!=2)]

#print np.where(Y==2)
X_test = X[:, np.where(Y == 2) ]

X_test = X_test[:, 0, :]
#print np.shape(X_test)
from sklearn import svm
from sklearn import cross_validation
#X = [[0, 0], [1, 1]]
#y = [0, 1]

X_dash = np.transpose(X_in)

#print np.shape(X_in)
#print np.shape(Y_in)
clf = svm.SVC()
#clf.fit(X_dash, Y_in)
scores = cross_validation.cross_val_score(clf, X_dash, Y_in, cv = 5)
print scores

#Y_out = clf.predict(np.transpose(X_test))
#print np.transpose(Y_out)


#Y_2 = np.array(115,2)
"""
for i in range(115):
    print Y_out[i]
    #Y_2[:,i] = i,Y_outv
"""
