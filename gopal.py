#I want sort data and diff of two number is 2.
#Same number should not repeat (example 8,10).

#I have data like (2,8,1,6,10,20,33,7,4,22)
#Output

#2,4
#6,8
#20,22

bb=(2,8,1,3,6,10,20,33,7,4,22)
a=(1,3,2,4,7,8,9)
b=sorted(a)

print(b)
c={}
for i in b:
    if (i+2) in b:
        #print(c.keys())
        #print(c.values())
        #print (i, i+2)
        if ((i in c.keys()) | (i in c.values()) ):
            #print("i found here", i)
            continue
        else:
            c[i]=i+2


for i in c.keys():
    print(i, c[i])