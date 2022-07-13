from datetime import date
from os import path
import time
import os
from datetime import datetime

black_this = [1,
        2,
              3]
path = './README.md'
exist =    os.path.exists(path)
print(exist)
print(time.time())
print(date.today())
print(datetime.today())
