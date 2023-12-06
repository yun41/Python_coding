T = int(input())

for test_case in range(T):
    N = int(input())
    m = []
    m = list(map(int, input().split()))
    result = 0
    while len(m) > 0:
        m_max = max(m)
        index_max = m.index(m_max)
        buy = m[:index_max]
        m = m[index_max + 1:]

        result += m_max*len(buy) - sum(buy)
    print(f"#{test_case+1} {result}")

# index 함수, sum 함수 기억