# use of finditer

import re
name="Python is world's best programming language "
for i in re.finditer("world's",name):
  ans=i.span()
  print(ans)
