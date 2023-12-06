# 오른쪽에 보이는 코드를 계산기처럼 동작하는 Caculator클래스를 작성해보시오

# Hint1. __init__ 함수 작성(사용)
# Hint2. sum메서드와 avg메서드 생성

# cal1 = Caculator([1,3,5,7,9])
# cal1.sum() #합계
# >> 25

# cal1.avg() #평균
# >> 5.0

# cal2 = Calculator([2,4,6,8,10])
# cal2.sum() #합계
# >> 30

# cal2.avg() #평균
# >> 6.0

class Calculator:
    def __init__(self, num):
        self.num=num

    def sum(self):
        sum=0
        for n in self.num:
            sum+=n
        
        return sum
        print(f"합계 : {sum}")

    def avg(self):
        total = self.sum()
        n = len(self.num)
        av = total/n
        print(f"평균 : {av}")


cal1 = Calculator([1,3,5,7,9])
cal2 = Calculator([2,4,6,8,10])

print(f"합계 : {cal1.sum()}")
cal1.avg()

print(f"합계 : {cal2.sum()}")
cal2.avg()