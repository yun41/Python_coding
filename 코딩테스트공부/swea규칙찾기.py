T = int(input())
for i in range(T):
    s = list(map(str, input()))
    for j in range(1, len(s)+1):
        if s[0] == s[j] and s[:j] == s[j:j*2]:
            print(f"#{i+1} {j}")
            break