sum_am = 0
list_am = []
print('세 자리의 암스트롱 수 : ',end='')

for i in range(100,999):
    hund_ = i//100
    tenth_ = i//10%10
    ones_ = i%100%10

    sum_am = (hund_**3)+(tenth_**3)+(ones_**3)

    if sum_am == i:
        print(i,end=' ')