n = list(map(int, input()))
sum = 0

for i in n:
    sum += i
    print(i)

print(sum)

# swea 대각선 출력하기
a = 0
for i in range(5):
    for j in range(5):
        if a == j:
            print("#", end="")
        else:
            print("+", end="")
    a += 1
    print()