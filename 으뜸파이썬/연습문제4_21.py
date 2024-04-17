y_m_d = input('주민등록번호 첫 6숫자 형식 입력 : ')

year = int(y_m_d[:2])
month = int(y_m_d[2:4])
day = int(y_m_d[4:6])

if year >= 50:
    year += 1900
else:
    year += 2000

print(f'{year}년 {month}월 {day}일')