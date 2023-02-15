import json
import sys
import timeit
import matplotlib.pyplot as plt
sys.setrecursionlimit(20000)
def func1(arr, low, high):

   if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= p:

           high = high - 1
        while low <= high and array[low] <= p:

           low = low + 1
        if low <= high:

           array[low], array[high] = array[high], array[low]
        else:

           break
    array[start], array[high] = array[high], array[start]
    return high


with open("ex2.json", "r") as inF:
    content = json.load(inF)

timeplot = []
for i in content:
    length = len(i)
    timing = timeit.timeit(lambda:func1(i, 0, length-1), number=1)
    timeplot.append(timing)

plt.plot(timeplot)
plt.title("Timing Plot")
plt.xlabel("Number of array")
plt.ylabel("In Seconds(Sec)")
plt.show()
