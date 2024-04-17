def sum_range(n1,n2):
    sum_n = 0
    for n in range(n1,n2+1):
        sum_n += n
    print(f'{n1}에서 {n2}까지의 정수의 합 : {sum_n}')

sum_range(10,20)
sum_range(40,100)