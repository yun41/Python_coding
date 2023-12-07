# 내 풀이
# N = int(input())
# fear = list(map(int, input().split()))
# count = 0

# fear.sort() # sort()는 기본적으로 오름차순

# while len(fear) > 0:
#     for i in range(max(fear)):
#         fear.pop()
#     count += 1

# print(count)


# 답지
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)