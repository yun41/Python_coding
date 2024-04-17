a = int(input('범위의 시작 정수 : '))
b = int(input('범위의 마지막 정수 : '))

multi = 1
for i in range(a,b+1):
    multi *= i

list_bool = []

for j in range(b+1,multi+1):
    list_bool = []
    for k in range(a,b+1):
        if j%k==0:
            list_bool.append(True)
    
    if len(list_bool)==((b-a)+1):
        if False in list_bool:
            continue
        else:
            list_multi_num = j
            break

print(f'{a}에서 {b}까지의 정수들의 최소 공배수는 :',list_multi_num)