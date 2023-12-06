# word.show_question()
# word.check_answer(int(input("=> ")))

# 출력 결과
# " 얼죽아 "의 뜻은?
# 1. 얼어 죽어도 아메리카노
# 2. 얼굴만은 죽어도 아기피부
# => 1
# 정답입니다.

class Word:
    def __init__(self, new, b1, b2, ans):
        self.new = new
        self.b1 = b1
        self.b2 = b2
        self.ans = ans

    def show_question(self):
        print(f'"{word.new}" 의 뜻은?')
        print(f"1. {word.b1}")
        print(f"2. {word.b2}")

    def check_answer(self, a):
        if a==word.ans:
            print("정답")
        else:
            print("오답")

word = Word("얼죽아","얼어 죽어도 아메리카노","얼굴만은 죽어도 아기피부",1)
# word = Word("혼코노", "혼자서는 코딩 노노", "혼자 코인 노래방", 2)
# word = Word("애빼시", "애교 빼면 시체", "애들은 빼빼로 시시해", 1)

word.show_question()
word.check_answer(int(input("=>")))