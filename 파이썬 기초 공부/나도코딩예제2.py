# Quiz) 행맨 게임(영어 단어 퀴즈) 프로그램을 만드시오
# -리스트에 3개 이상의 단어를 추가
# (예) apple, banana, orange
# -위 리스트에서 랜덤으로 1개의 단어를 선택
# -단어의 길이에 맞게 밑줄 출력                                                                         -okay
# (예) apple 의 경우 _ _ _ _ _
# -사용자로부터 1글자씩 입력을 받되, 단어에 입력값이 포함되면 'Correct' 출력, 아니면 'wrong' 출력
# -매번 입력을 받을 때마다 현재까지 맞힌 글자를 표시 (맞히지 못한 글자는 밑줄 출력)
# (예) a 입력 시 : a _ _ _ _
#     p 입력 시 : a p p _ _
#     c 입력 시 : a p p _ _
# -정답을 맞히면 Success 출력 후 프로그램 종료 (단, 횟수 제한은 없음)


import random
words = ['apple', 'banana', 'orange']
word = random.choice(words)
letters=""

while True:
    succeed = True
    for a in word:
        if a in letters:
            print(a, end=" ")
        else:
            print('_', end=" ")
            succeed=False

    if succeed:
        print("\nSuccess")
        break

    ans = input("\n\n단어를 입력하세요: ")
    if ans in word:
        print('Correct')
    else:
        print('Wrong')

    if ans not in letters:
        letters+=ans