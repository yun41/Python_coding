def mean3(a,b,c):
    return (a+b+c)/3

def max3(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c
        
def min3(a,b,c):
    if a<b:
        if a<c:
            return a
        else:
            return c
    else:
        if b<c:
            return b
        else:
            return c 

def mean6(a,b,c,d,e,f):
    return (mean3(a,b,c)*3+mean3(d,e,f)*3)/6

def max6(a,b,c,d,e,f):
    if max3(a,b,c) > max3(d,e,f):
        return max3(a,b,c)
    else:
        return max3(d,e,f)
    
def min6(a,b,c,d,e,f):
    if min3(a,b,c) < min3(d,e,f):
        return min3(a,b,c)
    else:
        return min3(d,e,f)
    
a,b,c,d,e,f = map(int, input('여섯 개의 수를 입력하시오 : ').split())
print('평균값은',mean6(a,b,c,d,e,f))
print('최댓값은 ',max6(a,b,c,d,e,f))
print('최솟값은',min6(a,b,c,d,e,f))