import timeit
import matplotlib.pyplot as plt

cache = {1:0, 2:1}
def fib(n):
    if n not in cache.keys():
        cache[n] = fib(n-1) + fib(n-2)
    return cache[n]

time_mem = []
for x in range(1,35):
    timing = timeit.timeit(lambda:fib(x), number=1)
    time_mem.append(timing)

def fib1(n):
    if n == 0 or n ==1:
        return n
    else:
        return fib1(n-1) + fib1(n-2)

time_reg = []

for x in range(1,35):
    timing2 = timeit.timeit(lambda:fib1(x), number=1)
    time_reg.append(timing2)


plt.plot(time_reg, label="Without Memoization")
plt.plot(time_mem, label="With Memoization")
plt.legend(loc="upper left")
plt.title("Timing Plot")
plt.xlabel("Number of n")
plt.ylabel("In Seconds(Sec)")
plt.show()