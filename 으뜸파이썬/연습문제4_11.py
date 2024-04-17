x1 = int(input("x1 좌표를 입력하시오 : "))
y1 = int(input("y1 좌표를 입력하시오 : "))
x2 = int(input("x2 좌표를 입력하시오 : "))
y2 = int(input("y2 좌표를 입력하시오 : "))

def area(x1,y1,x2,y2):
    return abs(x1-x2)*abs(y1-y2)/2

print('직각삼각형의 면적은 :',area(x1,y1,x2,y2))