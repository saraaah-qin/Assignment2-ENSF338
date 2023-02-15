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
    mid = start + (end - start) // 2

    if array[start] > array[mid]:
        array[start], array[mid] = array[mid], array[start]
    if array[start] > array[end]:
        array[start], array[end] = array[end], array[start]
    if array[mid] > array[end]:
        array[mid], array[end] = array[end], array[mid]
    pivot = array[mid]
    
    i = start - 1
    for j in range(start, end):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[end] = array[end], array[i+1]
    return i+1


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
