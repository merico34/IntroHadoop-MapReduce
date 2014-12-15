#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        #ip, id, username, time, req, status, size, aa, bb, cc =  data
        #req, size = data
	#print "{0}\t{1}".format(req, size)
	print "{0}\t{1}".format(data[0], data[9]) #0: IP, 6:uri, 9:size

