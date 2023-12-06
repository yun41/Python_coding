a=10

def f():
    global a
    a=0
    return True

print(True or f())

True or f() #왼쪽이 이미 true 이기 때문에 f()값은 계산되지 않음
False and f() #왼쪽이 이미 False 이기 때문에 f()값은 계산되지 않음

position=(3.15, 2.5, 7.5)
x,y,z = position

print(x)