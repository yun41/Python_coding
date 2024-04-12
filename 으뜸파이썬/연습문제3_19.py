print('맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.\n- 햄버거(입력 b)\n- 치킨(입력 c)\n- 피자(입력 p)')
chosen_menu = input('메뉴를 선택하세요(알파벳 b, c, p 입력) : ')
b = True

while chosen_menu not in ['b','c','p']:
    chosen_menu = input('메뉴를 다시 입력하세요(알파벳 b, c, p 입력) : ')

if chosen_menu == 'b':
    print('햄버거를 선택하였습니다.')
elif chosen_menu == 'c':
    print('치킨을 선택하였습니다.')
elif chosen_menu == 'p':
    print('피자를 선택하였습니다.')