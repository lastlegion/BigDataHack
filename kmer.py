import csv
with open("1.csv", "rb") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        seq = str(row["seqs"])
        n_mer = []
        x=0
        N = 3

        hist = []* (4**N)
        while x < len(seq):
            x = x+N
            #print seq[x-N:x]
            n_mer.append(seq[x-N: x])
            n_mer.sort()
            print n_mer
