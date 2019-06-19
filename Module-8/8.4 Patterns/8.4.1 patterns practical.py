import re
import sys
pattern = 'Fred'
file=open("test.txt","r")

regexp=re.compile(pattern)
for line in file:
    match = regexp.search(line)
    if match:
        print(line)