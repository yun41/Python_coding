class BlackBox():
    pass

b1=BlackBox()
b1.name = '까망이' #변수 선언
print(b1.name)
print(isinstance(b1, BlackBox))

b2=BlackBox()
print(b2.name) #객체를 아직 만들어주지 않음


class BlackBox():
    def __init__(self, name, price): #__init__() 초기화
        self.name = name    #self.name : 멤버변수
        self.price = price  #self.price : 멤버변수 - 서로 독립적인 객체
    def set_travel_mode(self, min):     #여행 모드 시간 (분)
        #print(str(min) + '분 동안 여행 모드 ON')
        print(f'{self.name} {min}분 동안 여행 모드 ON')

b1 = BlackBox('까망이', 200000)
b1.set_travel_mode(20)  #self에 b1객체가 들어감
print(b1.name, b1.price)
b2 = BlackBox('하양이', 100000)
b2.set_travel_mode(10)  #self에 b2객체가 들어감
print(b2.name, b2.price)

#상속은 class에서 코드를 그대로 받아올 수 있음
class TravelBlackBox(BlackBox): #BlackBox로부터 class 상속 받아온 것
    def set_travel_mode(self, min):
        print(str(min)+'분 동안 여행 모드 ON')
#BlackBox : 부모 클래스, TravelBlackBox : 자식 클래스

#상속 받아서 수정해서 사용 가능
class TravelBlackBox(BlackBox):
    def __init__(self, name, price, sd):
        #BlackBox.__init__(self, name, price)
        super().__init__(name, price)
        self.sd = sd

    def set_travel_mode(self, min):
        print(str(min) + '분 동안 여행 모드 ON')

#try
"""
try:
    수행문장
except:
    에러처리
else:
    정상동작
finally:
    마지막 수행

"""

num1=2
num2=3
try:
    result= num1/num2
    print(f'연산 결과는 {result}입니다')
except ZeroDivisionError:
    print('0으로 나눌 수 없어요')
except TypeError:
    print('값의 형태가 이상해요')
except Exception as err:
    print('에러가 발생했어요 : ', err)