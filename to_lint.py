import os
import time
from datetime import date, datetime
from os import path

black_this = [1, 2, 3]
path = "./README.md"
exist = os.path.exists(path)
print(exist)
print(time.time())
print(date.today())
print(datetime.today())
