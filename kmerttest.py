seq = 'prashanth'
x = 0
N = 3
n_mer = []
while x < len(seq)-N+1:
    #print seq[x-N:x]
    n_mer.append(seq[x: x+N])
    #n_mer.sort()
    x = x+1

print n_mer