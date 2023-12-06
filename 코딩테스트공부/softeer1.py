import sys
from collections import deque
T = int(input())
list = deque()
count = 0

for i in range(T):
  a,b = map(int, input().split())
  list.append(a)
  list.append(b)

for i in range(T):
       a = list.popleft()
       b = list.popleft()
       c =a + b
       print("Case #"+str(i+1)+ ": "+str(c))
