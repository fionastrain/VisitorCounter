#!/usr/bin/python

import sys
file = open("times.txt","r")
morning = file.readline().strip()

if morning == "":
    morning = 0
    afternoon = 0
    evening = 0
    night = 0
    aftermidnight = 0
else:
    morning = int(morning)
    afternoon = int(file.readline().strip())
    evening = int(file.readline().strip())
    night = int(file.readline().strip())
    aftermidnight = int(file.readline().strip())
print "<br/> Stats on Time of Visitors"
print "<br/> Morning: ", morning
print "<br/> Afternoon: ", afternoon
print "<br/> Evening: ", evening
print "<br/> Night: ", night
print "<br/> After Midnight: ", aftermidnight
file.close()
file = open("times.txt", "w")
hour = int(sys.argv[1])

if hour < 6:
    aftermidnight = aftermidnight + 1
elif hour < 12:
    morning = morning + 1
elif hour < 18:
    afternoon = afternoon +1 
else:
    night = night + 1

file.write(str(morning)+'\n')
file.write(str(afternoon)+'\n')
file.write(str(evening)+'\n')
file.write(str(night)+'\n')
file.write(str(aftermidnight)+'\n')
file.close()
