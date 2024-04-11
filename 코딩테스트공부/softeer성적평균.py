N, K = map(int, input().split())

S = list(map(int, input().split()))

for j in range(K):
    total = 0
    num = list((map(int, input().split())))
    num_list = S[num[0]-1:num[1]]
    difference = num[1] - num[0] + 1
    for i in range(difference):
        total += num_list[i]
    print(format(round(total/difference,2), ".2f"))