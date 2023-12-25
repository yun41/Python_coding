board = [
    [1,1,1,0,1,1,1],
    [0,0,0,0,0,1,1],
    [0,1,1,1,1,1,0],
    [0,0,1,1,1,1,1],
    [1,0,0,1,0,1,1],
    [1,0,1,1,1,0,1],
    [1,1,1,1,1,0,1],
    [1,0,1,0,0,1,1],
    [1,1,1,1,1,1,1],
    [1,0,1,1,1,1,1],
    [0,0,0,0,0,0,0]
]

T = int(input())

for i in range(1, T + 1):
    count = 0
    num = [0] * 5
    num_1 =[0] * 5
    list_num = list(map(int, input().split()))
    

    if list_num[0] > 9999:
        num_digit_1 = 5
    elif list_num[0] > 999:
        num_digit_1 = 4
        num[0] = 10
    elif list_num[0] > 99:
        num_digit_1 = 3
        num[0] = 10
        num[1] = 10
    elif list_num[0] > 9:
        num_digit_1 = 2
        num[0] = 10
        num[1] = 10
        num[2] = 10
    elif list_num[0] == 0:
        num_digit_1 = 0
        num[0] = 10
        num[1] = 10
        num[2] = 10
        num[3] = 10
        num[4] = 10
    else:
        num_digit_1 = 1
        num[0] = 10
        num[1] = 10
        num[2] = 10
        num[3] = 10

    for j in range(num_digit_1 - 1,-1,-1):
        num[4-j] = list_num[0] // (10**j)
        list_num[0] %= (10**j)
    
    
    if list_num[1] > 9999:
        num_digit = 5
    elif list_num[1] > 999:
        num_digit = 4
        num_1[0] = 10
    elif list_num[1] > 99:
        num_digit = 3
        num_1[0] = 10
        num_1[1] = 10
    elif list_num[1] > 9:
        num_digit = 2
        num_1[0] = 10
        num_1[1] = 10
        num_1[2] = 10
    elif list_num[1] == 0:
        num_1[0] = 10
        num_1[1] = 10
        num_1[2] = 10
        num_1[3] = 10
        num_1[4] = 10
    else:
        num_digit = 1
        num_1[0] = 10
        num_1[1] = 10
        num_1[2] = 10
        num_1[3] = 10

    for k in range(num_digit - 1,-1,-1):
        num_1[4-k] = list_num[1] // (10**k)
        list_num[1] %= (10**k)
    
    for num_index in range(5):
        if num[num_index] != num_1[num_index]:
            board_index_1 = num[num_index]
            board_index_2 = num_1[num_index]
            for board_index in range(7):
                if board[board_index_1][board_index] != board[board_index_2][board_index]:
                    count += 1
    
    print(count)