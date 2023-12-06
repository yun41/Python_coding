numbers= [6,12,8,10,7,2,3]
for a in numbers:
    if a<10:
        continue
    print(a)

for b in range(1,11):
    if b%3==0:
        continue
    else:
        print(b)