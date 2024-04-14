list_int = list(map(int, input('정수를 입력하시오 : ')))
list_int_reverse = [0]*len(list_int)

for j in range(len(list_int)):
    list_int_reverse[j] = list_int[len(list_int)-1-j]

if list_int == list_int_reverse:
    for i in list_int:
        print(i,end='')
    print('은(는) 거꾸로 정수입니다.')
else:
    for k in list_int:
        print(k,end='')
    print('은(는) 거꾸로 정수가 아닙니다.')