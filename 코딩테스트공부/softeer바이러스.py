import sys

k, p, n = map(int, sys.stdin.readline().split())

k %= 1000000007
for _ in range(n):
    k *= p % 1000000007
 
print(k)

# a * b mod m = ((a mod m) * (b mod m)) mod m