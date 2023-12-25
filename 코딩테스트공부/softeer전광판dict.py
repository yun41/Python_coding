# dictionary와 string을 이용한 풀이
board = {
    '0' : '1110111',
    '1' : '0000011',
    '2' : '0111110',
    '3' : '0011111',
    '4' : '1001011',
    '5' : '1011101',
    '6' : '1111101',
    '7' : '1010011',
    '8' : '1111111',
    '9' : '1011111',
    ' ' : '0000000'
}
T = int(input())

for _ in range(T):
    original_light, changed_light = map(str, input().split())

    # 문자열 결합
    original_light = ' '*(5-len(original_light)) + original_light
    changed_light = ' '*(5-len(changed_light)) + changed_light
    
    print(original_light)
    print(changed_light)

    count = 0
    for i in range(5):
        for j in range(7):
            if board[original_light[i]][j] != board[changed_light[i]][j]:
                count += 1
    
    print(count)