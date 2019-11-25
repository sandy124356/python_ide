a=list('12345678')

print(a)

print(type(a))

a[0]=a[6]=0

print(a)

a[1]=a[-7]

print(a)

a=''.join([str(i) for i in a])

print(a)

a='bcd'
b=list('abc')
a.join(b)

print(a)