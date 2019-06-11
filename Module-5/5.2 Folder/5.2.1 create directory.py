# create directory 

import os
os.chdir(r'E:/')
if not os.path.exists("MYFOLDER"):
   os.makedirs("MYFOLDER")
else:
   print("Already exists")
