pi = 3.14

def square(s):
    return s**3

def cube_(w,h,l):
    return w*h*l

def horn(r,h):
    global pi
    return (1/3)*pi*(r**2)*h

def ball(r):
    global pi
    return (4/3)*pi*(r**3)

def cylinder(r,h):
    global pi
    return pi*(r**2)*h

print('(1) 정육면체:',square(12))
print('(2) 정육면체:',square(20))
print('(3) 직육면체:',cube_(3,5,6))
print('(4) 원뿔:',horn(20,10))
print('(5) 구:',ball(15))
print('(6) 원기둥:',cylinder(20,10))