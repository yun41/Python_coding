lott = list(map(int, input('세 복권번호를 입력하시오 : ').split()))
count_ = 0

for i in range(3):
    if lott[i] == 2:
        count_ += 1
    elif lott[i] == 3:
        count_ += 1
    elif lott[i] == 9:
        count_ += 1

if count_ == 3:
    print('상금 1억 원')
elif count_ == 2:
    print('상금 1천만 원')
elif count_ == 1:
    print('상금 1만 원')
else:
    print('다음 기회에...')