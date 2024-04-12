sum = 0
num = int(input('숫자를 입력하세요 : '))

for i in range(1,num+1):
    sum += ((1/i)**2)

print('결과는 {}입니다.'.format(sum))