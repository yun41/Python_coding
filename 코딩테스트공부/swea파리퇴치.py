T = int(input())

def find_(x,y):
    if y+m <= n+1:
        element = 0
        for ele_ in range(m):
            for ele__ in range(m):
                element += map_[x+ele_][y+ele__]

        return element

for i in range(T):
    map_ = []
    storage = []
    result = []
    result_ = 0
    n, m = map(int, input().split())
    j = 0
    k = 0

    for _ in range(n):
        map_list = list(map(int, input().split()))
        map_.append(map_list)

    for j in range(n-m+1):
        for k in range(n-m+1):
            result.append(find_(j,k))

    print(f"#{i+1}", max(result))