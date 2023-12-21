import sys
number_list = list(map(int, sys.stdin.readline().split()))

for i in range(len(number_list)-1):
    if number_list[i] > number_list[i+1]:
        number_list[i] = 1
    elif number_list[i] < number_list[i+1]:
        number_list[i] = 0

if 1 not in number_list:
    print('ascending')
elif 0 not in number_list:
    print('descending')
else:
    print('mixed')