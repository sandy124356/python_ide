def functionA():
    print("a1")
    from weird import functionB
    print("now name is ", __name__)
    print("a2")
    functionB()
    print("a3")

def functionB():
    print("b")


print("name is ", __name__)



print("m1")
functionA()
print("m2")

print("t2")