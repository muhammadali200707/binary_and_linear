import time
from datetime import datetime

data = list(set([1, 1, 6, 13, 14, 14, 23, 23, 26, 26, 30, 31, 32, 32, 37, 42, 44, 47, 48, 50]))

len_data = len(data) - 1
data.sort()
print(data)

number = int(input("Enter your number -->  "))
low = 0
len_data = len(data) - 1
count = 0
print(f"This is the starting  time --> {datetime.now()}")
while True:
    time.sleep(0.2)
    count += 1
    middle_point = (len_data + low) // 2
    if data[middle_point] < number:  # false
        low = middle_point + 1
    elif data[middle_point] == number:
        print(number)
        print(f"Found in  {count} attempts")
        break

    else:
        len_data = middle_point

print(f"This is the ending  time --> {datetime.now()}")
