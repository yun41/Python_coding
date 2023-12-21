T = int(input())
start = 0
tri = []

for i in range(T):
    print(f"#{i+1}")
    N = int(input())
    for j in range(N):
        temp = tri
        tri = [0] * (j+1)
        tri[0] = 1
        tri[j] = 1

        if j>1:
            for n in range(1, j):
                tri[n] = temp[n-1] + temp[n]
                tri[j-n] = temp[j-n] + temp[j-n-1]
                if n > (j-n):
                    break
    
        print(*tri)