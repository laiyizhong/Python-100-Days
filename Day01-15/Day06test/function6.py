
def foo():
    a = 5
foo()
#print(a)

b = 100
def foo2():
    print(b)

foo2()

def foo3():
    b = 200
    print(b)

foo3()

def foo4():
    global b
    print(b)
    b = 300
    print(b)

foo4()
print(b)
