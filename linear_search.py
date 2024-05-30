import time
from datetime import datetime

data = [1, 4, 5, 7, 7,  12, 23, 25, 27, 27,  29, 30, 31, 33, 34, 36, 45, 58, 78, 78,  92, 100]
number = int(input("Enter your number ->  "))
counter = 0
print(f"This is the starting  time --> {datetime.now()}")
for i in data:
    time.sleep(0.2)
    counter += 1
    if i == number:
        print(f"Correct number --> {i}")
        break
print(f"Found after {counter} attempts")
print(f"This is the ending  time --> {datetime.now()}")



