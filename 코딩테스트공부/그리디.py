coin = [500, 100, 50, 10]
prize = 1260
count = 0

for c in coin:
    count += prize // c
    prize %= c

print(count)