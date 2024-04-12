star = int(input('숫자를 입력하세요 : '))

for i in range(1,star+1):
    print(' '*(star-i),end='')
    print('*'*i)