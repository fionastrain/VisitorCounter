#!/usr/bin/python

file = open ("numvisits.txt","r")
numdata = file.readline()
numdata = numdata.strip()

num = int(numdata)
file.close()
print num
