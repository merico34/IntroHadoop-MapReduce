#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import csv


reader = csv.reader(sys.stdin, delimiter='\t')
#writer = csv.writer(sys.stdout, delimiter='\t')
#,lineterminator='\n', quoting=csv.QUOTE_NONE)
#, quotechar='"', quoting=csv.QUOTE_ALL)

s = [',', '.', '!', '?', ':', ';', '"', '(', ')', '<', '>', '[', ']', '#', '$', '=', '-', '/', '\n', '\t', '\\', '|']

mylist = []
for line in reader:
    if line[0] == "id":  # ignore first line
    #if line[0] != "55975": #test
    	continue
    body = line[4]
    for x in s:
        body = body.replace(x," ")
    bodyvec = body.split(" ")
    for w in bodyvec:
        if w.strip() != "":
            print "{0}\t{1}".format(w.lower(), line[0])
    #mylist.append([len(body),line])
    
#mylist.sort()
    
#for i in range( max(0,len(mylist)-10), len(mylist) ):
#    writer.writerow(mylist[i][1])
#    print(mylist[i][1])

#print(body)





