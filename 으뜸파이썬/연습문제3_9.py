num = int(input('정수를 입력하시오 : '))
num_bool_2 = False
num_bool_3 = False

if num%2==0:
    print(f'{num}는(은) 2(으)로 나누어집니다.')
    num_bool_2 = True
else:
    print(f'{num}는(은) 2(으)로 나누어지지 않습니다.')

if num%3==0:
    print(f'{num}는(은) 3(으)로 나누어집니다.')
    num_bool_3 = True
else:
    print(f'{num}는(은) 3으로 나누어 지지 않습니다.')

if num_bool_2 and num_bool_3:
    print(f'{num}는(은) 2와(과) 3 모두로 나누어집니다.')
else:
    print(f'{num}는(은) 2와(과) 3 모두로 나누어지지 않습니다.')