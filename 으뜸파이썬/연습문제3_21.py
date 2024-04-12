num = int(input('숫자를 입력하세요 : '))
is_num = 0

for i in range(3,num,2):
    if num%2==0:
        is_num = 1
    elif num%i==0:
        is_num = 1

if is_num == 0:
    print(f'{num}는 소수입니다')
elif is_num == 1:
    print(f'{num}는 소수가 아닙니다')