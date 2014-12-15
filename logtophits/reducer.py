#!/usr/bin/python

import sys

fileMax = 0
fileMaxName = ""
fileHit = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisfile = data_mapped

    if oldKey and oldKey != thisKey:
        if fileHit > fileMax:
		fileMax = fileHit
		fileMaxName = oldKey
        oldKey = thisKey;
        fileHit = 0

    oldKey = thisKey
    fileHit +=1

if oldKey != None:
    print fileMaxName, "\t", fileMax

