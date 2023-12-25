# join함수는 list를 문자열화 시켜줌
m,n,k = map(int, input().split())
secret_manual = ''.join(list(map(str, input().split())))
order_button = ''.join(list(map(str, input().split())))

print(secret_manual)
print(order_button)

if m > n:
    print('normal')
    exit()

# in의 역할 다시 공부
if secret_manual in order_button:
    print('secret')
else:
    print('normal')


# 굳이 index 넣어가며 찾지말고 바로 찾기