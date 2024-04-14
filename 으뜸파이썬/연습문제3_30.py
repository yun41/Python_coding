print('1)덧셈\t2)뺄셈\t3)곱셈\t4)나눗셈')
num = int(input('어떤 연산을 원하는지 번호를 입력하세요 : '))

if num < 5:
    print('연산을 원하는 숫자 두개를 입력하세요')
    num_1 = int(input())
    num_2 = int(input())

if num == 1:
    print(f'{num_1} + {num_2} = {num_1+num_2}')
elif num == 2:
    print(f'{num_1} - {num_2} = {num_1-num_2}')
elif num == 3:
    print(f'{num_1} * {num_2} = {num_1*num_2}')
elif num == 4:
    print(f'{num_1} / {num_2} = {num_1/num_2}')
else:
    print('잘못 입력하였습니다.')