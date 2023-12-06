age = int(input('나이를 입력하세요 : '))
score = int(input('점수를 입력하세요 : '))

if age>=20:
    if score>=80:
        print("합격입니다!")
    else:
        print("점수가 낮아 불합격입니다!")
else:
    print("너무 어려서 불합격입니다.")