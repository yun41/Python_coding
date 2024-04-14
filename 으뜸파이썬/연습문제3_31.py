for num in range(1,20001):
    sum_num = 0
    sum_num_1 = 0
    for i in range(1,num):
        if num%i==0:
            sum_num += i
    for j in range(1,sum_num):
        if sum_num%j==0:
            sum_num_1 += j
    
    if sum_num_1 == num:
        print(f'{num}의 친화수 {sum_num}')