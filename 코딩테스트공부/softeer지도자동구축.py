import sys
input = sys.stdin.readline

N = int(input())
a = 2

for i in range(N):
    a += (a - 1)

print(a**2)