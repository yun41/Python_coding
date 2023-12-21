# 배낭의 무게 = W
# 귀금속 종류 = N
# i + 1 번째 줄에는 i 번째 금속의 무게 M와 무게당 가격 P
# 2번째 줄에는 1번째 금속의 무게와 무게당 가격

import sys
input = sys.stdin.readline  # 이게 있어야 반복문으로 input을 받을 때 시간 초과가 안생긴다
w, n = map(int, input().split())
cost = 0

m_p = [list(map(int, input().split())) for _ in range(n)]
m_p.sort(key = lambda x : x[1], reverse = True)

for m, p in m_p:
    if w >= m:
        cost += (m * p)
        w -= m
    else:
        cost += (w * p)
        break

print(cost)