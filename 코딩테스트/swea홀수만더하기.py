T = int(input())

# for i in range(T):
#     s = list(map(int, input().split()))
#     result = 0

#     for j in range(len(s)):
#         if s[j] % 2 == 1:
#             result += s[j]

#     print(f"#{i+1} {result}")

for i in range(T):
    s = list(map(int, input().split()))
    result = 0

    for j in s:
        if j % 2 == 1:
            result += j

    print(f"#{i+1} {result}")

# 시간이 중요하므로 필요없는 과정 넣지 않기