T = int(input())

for i in range(T):
    m = list(map(int, input().split()))

    n = round(sum(m) / len(m))

    print(f"#{i+1} {n}")

# 반올림은 round 함수 round(올릴 수, 최종 자리 수 (1 = 소수 첫째 자리,0 = 일의 자리, -1 = 십의 자리))
# 올림은 ceil, 내림은 floor