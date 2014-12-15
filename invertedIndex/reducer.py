#!/usr/bin/python

import sys

fantastically_ids = []
count_fantastic = 0

for line in sys.stdin:

    data_mapped = line.strip().split("\t")

    if len(data_mapped) != 2:
        continue

    if data_mapped[0] == "fantastic":
        count_fantastic = count_fantastic + 1

    if data_mapped[0] == "fantastically":
        fantastically_ids.append(int(data_mapped[1]))

fantastically_ids = sorted(fantastically_ids)

print "count_fantastic: ", "\t", count_fantastic
print "fantastically_ids: ", "\t", fantastically_ids




























