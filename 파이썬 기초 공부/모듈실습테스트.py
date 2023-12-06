# import calendar
# print(calendar.month(2020,12))
# print(calendar.weekday(2020,12,1))
# print(calendar.monthrange(2020,12))

import random

for i in range(3): # 가위바위보 실행 횟수 지정
    sel = int(input("<<0(가위) 1(바위) 2(보)중 하나를 선택하세요>>\n"))
    ai = random.randrange(0,2)
    print(ai)
    if ai == sel:
        print("비겼습니다")
    elif ai > sel:
        print("졌습니다")
    elif ai == 0 and sel == 2:
        print("졌습니다")
    else:
        print("이겼습니다")