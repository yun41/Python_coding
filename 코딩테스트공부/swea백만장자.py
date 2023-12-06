T = int(input())

for test_case in range(T):
    result = 0
    N = int(input())
    m = list(map(int, input().split()))
    count = 0
    for i in range(N):
        count += 1
        if m[0] == max(m):
            result += (max(m) * (count-1))
            m.reverse()
            m.pop()
            m.reverse()
            count = 0
        elif m[0] == min(m):
            result -= min(m)
            m.reverse()
            m.pop()
            m.reverse()
    print(f"#{test_case+1}",result)

# 시간 초과