is_num = 0

for i in range(2,13):
    for n in range(3,i,2):
        if i%2==0:
            is_num = 1
        elif i%n==0:
            is_num = 1
    
    if is_num == 1:
        print(f'{i} : 소수')
    if is_num == 0:
        print(f'{i} : 합성수')