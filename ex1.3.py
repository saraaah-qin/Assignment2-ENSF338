cache={1:0,2:1}

def fib(n):

    if n not in cache.keys():
        cache[n]=fib(n-1)+fib(n-2)
    
    return cache[n]

