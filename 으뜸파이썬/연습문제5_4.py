a = [2,3,4,5,6]
print(a)
rev_a = []
for i in range(len(a)):
    rev_a.append(a.pop())
print(rev_a)