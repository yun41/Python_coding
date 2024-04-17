n_list = [10,20,30,50,60]
print('리스트 원소들 : {}'.format(n_list))

for i in range(len(n_list)-1):
    if n_list[i] < n_list[i+1]:
        n_list[i], n_list[i+1]= n_list[i+1], n_list[i]

print(n_list)
print('리스트 원소들 중 최솟값 : {}'.format(n_list[-1])) 