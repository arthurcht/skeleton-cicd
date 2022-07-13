import os
import time
from datetime import datetime
import time
from datetime import date

path = "./README.md"
exist =        os.path.exists(path)

print(exist)
print(time.time())
print(date.today())
print(datetime.today())