#modifiers

import re

print("match function")
print(re.match(r'dog','DOG dog cat',re.IGNORECASE))

print("search function")
print(re.search(r'dog','cat dog cat',re.IGNORECASE))

