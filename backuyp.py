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
    print i
    hist[i] = 0
X = np.zeros([64,431])
Y = np.zeros([431])

#print X[63,429]

linenum = 0
#print hist['aaa'], hist['aat']
with open("chicken_train.csv", "rb") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        for i in keywords:
            hist[i] = 0

        print linenum
        id = row["ID"]
        if id == '':
            id = 2
            print "-----"
            break
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



print 'Y', Y
print 'X', X


from sklearn import svm

#X = [[0, 0], [1, 1]]
#y = [0, 1]

X_dash = np.transpose(X)

clf = svm.SVC()
clf.fit(X_dash, Y)



X_test = np.zeros([64,200])
y_predicted = []

print("Finished training")

linenum = 0
with open("chicken_test.csv", "rb") as csvfile:
    print "sadfsadfdsaf"
    reader = csv.DictReader(csvfile)
    for row in reader:

        for i in keywords:
            hist[i] = 0

        print linenum
        id = row["ID"]
        if id == '':
            id = 2
            print "-----"
            break
        #Y[linenum] = int(id)
        seq = str(row["seqs"])
        print seq
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
            X_test[i, linenum] = hist[keywords[i]]

        y_pred = clf.predict(X_test)
        print " ===== "
        print y_pred
        linenum += 1
        if(linenum == 200):
            break







#Y_PREDICTED = clf.predict(


#pickle the array
#np.savetxt('Yrun1.txt', Y, fmt='%4.0f',delimiter=',', newline='\n')

#np.savetxt('Xrun1.txt', X, fmt='%4.0f',delimiter=',', newline='\n')

