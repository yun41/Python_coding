T = int(input())
cod = []

for i in range(64):
    cod[i] = ''

for test_case in range(1, T + 1):
    for i in range(26):
        su = chr(ord('A')+i)
        sd = chr(ord('a')+i)
        cod[i] = su
        cod[i+26] = sd
        if i < 10:
            cod[i+52] = str(i)
    cod[62] = '+'
    cod[63] = '/'
 
    inp = input()
    result = ''
    for i in range(len(inp)):
        num = cod.index(inp[i])
        binNum = str(bin(num)[2:])
        binNum = '0'*(6-len(binNum))+binNum
        result += binNum
    answer = ''
 
    for i in range(0, len(result), 8):
        e = int(result[i:i+8], 2)
        answer += chr(e)
    print(f'#{test_case} {answer}')