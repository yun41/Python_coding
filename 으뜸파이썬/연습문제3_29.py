tank = 500

while tank >= 50:

    list_change = list(map(str, input('충전 또는 사용한 연료를 +/- 기호와 함께 입력하시오 : ')))
    num = 0

    for i in range(1,len(list_change)):
        num += int(list_change[i])*10**(len(list_change)-1-i)

    if list_change[0] == '+':
        tank += num
    elif list_change[0] == '-':
        tank -= num
    
    print('현재 탱크양은 {} 입니다.'.format(tank))

print('경고 : 연료가 10% 미만이니 충전하세요!')