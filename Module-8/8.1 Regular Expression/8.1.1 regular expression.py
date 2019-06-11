# regular expression

import re

Nameage="""Rany is 23 and Jeny is 65, Tom is 85 and Roy is 42 """
age=re.findall(r'\d{1,3}',Nameage)
names=re.findall(r'[A-Z][a-z]*',Nameage)

ageDict={}
a=0

for eachname in names:
  ageDict[eachname] = age[a]
  a+=1
  
print(ageDict)
