hr = 0
min = 0

for i in range(5):
    n, m = list(map(str, input().split()))
    
    hr_n = int(n[:2])
    hr_m = int(m[:2])

    min_n = int(n[3:])
    min_m = int(m[3:])

    hr += hr_m - hr_n
    min += min_m - min_n

sum_hr = hr * 60

result = sum_hr + min
print(result)