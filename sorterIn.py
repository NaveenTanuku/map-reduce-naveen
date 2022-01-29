# Author: Naveen Tanuku
# Created: 28 Jan 2022
# Updated: 28 Jan 2022
# A simple sorter program

m = open("outputMapper.txt","r")  # open file, read-only
s = open("outputSorter.txt", "w") # open file, write

lines = m.readlines()
lines.sort()
for line in lines:
    s.write(line)

m.close()
s.close()

