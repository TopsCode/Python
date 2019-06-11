# delete directory

import os
os.chdir(r'E:/')
if os.path.exists("MYFOLDER"):
  os.rmdir("MYFOLDER")
