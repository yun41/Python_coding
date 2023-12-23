T = int(input())

def f_t():
    for x in range(round(l/2)):
        if n[x] == n[l-1-x]:
            return True
        else:
            return False

for i in range(T):
    n = list(map(str, input()))
    l = len(n)
    if f_t() == True:
        print(f"#{i+1}", 1)
    else:
        print(f"#{i+1}", 0)