import sys

n = int(input())
graph = []
result = []
number_block = 0

for _ in range(n):
    graph.append(list(map(int, input())))

def find_block(x,y):
    count = 0
    if x < 0 or x >= n or y < 0 or y >= n:
        return 0
    
    if graph[x][y] == 1:
        graph[x][y] = 2
        count += 1
        count += find_block(x-1,y)
        count += find_block(x+1,y)
        count += find_block(x, y+1)
        count += find_block(x, y-1)
        return count
    else:
        return 0
    
for i in range(n):
    for j in range(n):
        a = find_block(i,j)
        if a != 0:
            result.append(a)

result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])