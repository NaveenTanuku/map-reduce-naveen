s = open("outputSorter.txt", "r")
r = open("outputReducer.txt", "w")

thisKey=""
thisValue = 0.0

for line in s:
    data = line.strip().split('\t')
    store, amount = data
    if store!= thisKey:
        if thisKey:
            r.write(thisKey + '\t' + str(thisValue)+'\n')
        count = 0
        thisKey = store
        thisValue = 0.0
    count+=1
    thisValue += float(amount)
r.write(thisKey + '\t' + str(thisValue)+'\n')

s.close()
r.close()