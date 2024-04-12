alphabet = input('알파벳을 입력하시오 : ')

if alphabet in ['a','e','i','o','u']:
    print(f'{alphabet} (은)는 모음입니다.')
else:
    print(f'{alphabet} (은)는 자음입니다.')