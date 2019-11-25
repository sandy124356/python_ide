import time
import math
def prime(var):
    if var==1:
        return "false"
    for i in range(2,math.floor(math.sqrt(var))+1):
        #print("input is" , var, i)
        if var%i==0:
            return "false"
    return "true"



t=time.time()
for i in range(1,2000+1):
    print(i, prime(i))
print(time.time()-t)

