a=input()
print(a)
b = a.split()
b=b
#print(b.__class__)
#for i in b:
#    print(i)
#    print(''.join(sorted(i)))
for i in range(0,len(b)):
    a1 = ''.join(sorted(b[i]))
    #print(a1)
    for j in range(i+1, len(b)):
        a2 = ''.join(sorted(b[j]))
        #print(a1, " & ", a2)
        if a1 == a2:
            # print("i got", b[j], "and" , b[i])
            d={b[i],b[j]}

            print(d)

