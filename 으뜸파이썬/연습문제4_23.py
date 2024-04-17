def area_and_circumference(r):
    area = r**2*(3.14)
    circumference = 2*r*(3.14)
    return area, circumference

i = int(input('반지름을 입력하시오: '))
while i > 0:
    a,c = area_and_circumference(i)
    print('넓이 : {:7.3f}, 둘레 : {:7.3f}'.format(a,c))
    i = int(input('반지름을 입력하시오: '))
print('프로그램을 종료합니다.')