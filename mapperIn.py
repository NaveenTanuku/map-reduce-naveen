# Author: Naveen Tanuku
# Created: 28 Jan 2022
# Updated: 28 Jan 2022
# A simple map reduce program

f = open("purchase.txt","r")  # open file, read-only
o = open("outputMapper.txt", "w") # open file, write
for line in f:  
    rowList = line.strip().split("    ") # DT: List of Lists
    print (rowList )
    print (len(rowList ))
    if len(rowList) == 6:
        date, time, location, dept, amount, payType = rowList
        #assign names
        print ("{0}\t{1}".format(location, amount))
        o.write("{0}\t{1}\n".format(location, amount))
f.close()
o.close()
