

import time
import shutil
import os

second = time.time()
print(second)
localtime = time.localtime(second)
print(time.localtime(second))
print(localtime.tm_year)

asctime = time.strftime('%Y-%m-%d %H:%M:%S',localtime)
print(asctime)

mydate = time.strptime('2018-1-1', '%Y-%m-%d')
print(mydate)

