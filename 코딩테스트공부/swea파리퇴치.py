T = int(input())
map_ = []
storage = []
result = []
result_ = 0

def find_(x,y):
    if x < 0 or x >= n + 1 or y < 0 or y >= n + 1:
        return False
    if y+m <= n+1:
        element = 0
        for ele_ in range(m):
            element += map_[x+ele_][y]
        for ele__ in range(1,m):
            element += map_[x][y+ele__]
        for ele___ in range(1,m):
            element += map_[x+ele___][y+ele___]
        return element


for i in range(T):
    n, m = map(int, input().split())
    for _ in range(n):
        map_list = list(map(int, input().split()))
        map_.append(map_list)

    for j in range(n-m):
        for k in range(n-m):
            result.append(find_(j,k))
            
    max_ = max(result)
    print(f"#{i+1}", max_)