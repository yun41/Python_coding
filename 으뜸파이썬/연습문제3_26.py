n = int(input('n을 입력하시오 : '))

for i in range(1,n+1):
    if i%2!=0:
        for j in range((i-1)*n+1,i*n+1):
            print(j,end=' ')
    else:
        for k in range(i*n,(i-1)*n,-1):
            print(k,end=' ')
    print("\n")