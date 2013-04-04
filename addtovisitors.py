#!/usr/bin/python

file = open("numvisits.txt", "r")
numdat = file.readline()
numdat = numdat.strip()
if numdat == "":
    newnum = 0
else:
    num = int(numdat) 
    newnum = num + 1
file.close()
file = open("numvisits.txt", "w")
file.write(str(newnum))
file.close()
