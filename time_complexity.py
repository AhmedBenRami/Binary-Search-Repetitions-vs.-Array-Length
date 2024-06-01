import math
import matplotlib.pyplot as plt
import numpy as np

repeat = 0

def search(arr, target, start, end):
    global repeat
    
    middle = (start + end) // 2

    if target == arr[middle]:
        #print("found")
        return 0
    elif start > end:
        #print("not found")
        return 1
    else:
        repeat += 1
        if target > arr[middle]:
            return search(arr, target, middle + 1, end)
        else:
            return search(arr, target, start, middle - 1)


arr = [1]
repeats = [0]
for i in range(99999):
    arr.append(i)
    repeat = 0
    search(arr, arr[-1], 0, len(arr) - 1)
    repeats.append(repeat)


x = np.array(arr)
y = np.array(repeats)

plt.plot(x, y)
plt.xlabel('Array Length')
plt.ylabel('Number of Repetitions')
plt.title('Binary Search Repetitions vs. Array Length')


plt.plot([math.log(i,2) for i in range(1,99999)])
plt.show()
