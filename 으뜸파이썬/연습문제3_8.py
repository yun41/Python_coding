x,y = map(int, input('점의 좌표 x, y를 입력하시오 : ').split())

if x>0:
    if y>0:
        print('1사분면에 있음')
    elif y<0:
        print('4사분면에 있음')
elif x<0:
    if y>0:
        print('2사분면에 있음')
    elif y<0:
        print('3사분면에 있음')