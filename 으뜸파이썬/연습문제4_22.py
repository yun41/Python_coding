import datetime

date = datetime.datetime.now()

y,m,d = date.year, date.month, date.day
print('현재 시간은 {}년 {}월 {}일입니다.'.format(y,m,d))
print('지금 태어난 아이의 주민등록번호 앞자리는 : {}{}{}'.format(y-2000,m,d))