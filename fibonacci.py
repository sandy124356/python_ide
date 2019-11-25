from functools import lru_cache

cache_fib = {}
def fibo(x):
    if type(x)!=int:
        raise TypeError("type mismatch")
    if x<0:
        raise ValueError("value should be positive")
    if x in cache_fib:
        return cache_fib[x]
    if x==1:
        return 0
    elif x==2:
        return 1
    elif x>2:
        cache_fib[x]=fibo(x-2)+fibo(x-1)
        return fibo(x-2)+fibo(x-1)


for i in range(1,20):
    print(i,':',fibo(i))

for i in cache_fib.items():
    print(i)

#fibo("-2")