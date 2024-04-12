len_well = 30
len_snail, day = 0, 0

while len_snail < len_well:
    len_snail += 7
    day += 1
    print('day : {:3d} \t달팽이의 위치 : {:3d}미터'.format(day, len_snail))
    if len_snail < len_well:
        len_snail -= 5