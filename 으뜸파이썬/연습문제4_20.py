def fibo(n):
    if n<=1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
    
for i in range(16):
    print('fibo({:3d}) ={:10}'.format(i,fibo(i)))