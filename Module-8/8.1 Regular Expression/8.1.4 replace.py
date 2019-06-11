# replace string 

import re
word="dog, bot , god , rose , not "
regex=re.compile("[b]ot")
word=regex.sub("Sample",word)
print(word)
