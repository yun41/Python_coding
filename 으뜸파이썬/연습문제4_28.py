def factorial(k):
    if k<=1:
        return 1
    else:
        return k*factorial(k-1)

def euler(n):
    sum_euler = 0
    for i in range(n+1):
        sum_euler += (1/factorial(i))
    return sum_euler

print('euler( 5) = {:10.5f}'.format(euler(5)))
print('euler(20) = {:10.5f}'.format(euler(20)))