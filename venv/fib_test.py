from functools import lru_cache

dic = {}
def fib(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        if x in dic.keys():
            return dic[x]
        else:
            dic[x]= fib(x-1) + fib(x-2)
            return fib(x-1) + fib(x-2)

for i in range(100):
    print(fib(i))



