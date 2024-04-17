x1 = int(input("x1 좌표를 입력하시오 : "))
y1 = int(input("y1 좌표를 입력하시오 : "))
x2 = int(input("x2 좌표를 입력하시오 : "))
y2 = int(input("y2 좌표를 입력하시오 : "))

def distance(x1,y1,x2,y2):
    dis = (x1-x2)**2+(y1-y2)**2
    dis **= (1/2)
    return dis

print('두 점의 거리:',distance(x1,y1,x2,y2))