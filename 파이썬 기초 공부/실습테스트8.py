a=1
sum=0

while a<=100:
    if a%4==0:
        sum += a
        a=a+1
    else:
        a=a+1
        continue 

print(sum)