print('맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.\n1) 햄버거\n2) 치킨\n3) 피자')
chosen_menu = int(input('1에서 3까지의 메뉴를 선택하세요 : '))

while chosen_menu < 1 or chosen_menu > 3:
    chosen_menu = int(input('메뉴를 다시 입력하세요 : '))

if chosen_menu == 1:
    print('햄버거를 선택하였습니다.')
elif chosen_menu == 2:
    print('치킨을 선택하였습니다.')
elif chosen_menu == 3:
    print('피자를 선택하였습니다.')