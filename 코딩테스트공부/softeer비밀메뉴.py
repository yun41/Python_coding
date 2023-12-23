# join함수는 list를 문자열화 시켜줌
m,n,k = map(int, input().split())

if m > n:
    print('normal')
    exit()

secret_manual = ''.join(list(map(str, input().split())))
order_button = ''.join(list(map(str, input().split())))

print(order_button)

if secret_manual in order_button:
    print('secret')
else:
    print('normal')