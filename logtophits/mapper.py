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
	
	uri = data[6].split("/")
	depth = len(uri)
	#get rid of firsts elements (http://truc/...)
	if uri[0] == "http":
		deb = 3
	else:
		deb = 0
	uri2 = ""
	for i in range(deb,len(uri)):
		uri2 = uri2 + uri[i] + "/"
	print "{0}\t{1}".format(uri2, data[9]) #0: IP, 6:uri, 9:size

