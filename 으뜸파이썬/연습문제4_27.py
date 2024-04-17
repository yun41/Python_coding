def unit_fraction(frac):
    i=1
    bool_frac = True
    while bool_frac == True:
        if abs(frac - (1/i)) > abs(frac - (1/(i+1))):
            i+=1
        else:
            bool_frac = False
    return i

f=float(input('1보다 작고 0보다 큰 소수를 입력하세요: '))
print('가장 가까운 단위분수는 1/{}이며, 이 값은 {}입니다.'.format(unit_fraction(f),1/unit_fraction(f)))