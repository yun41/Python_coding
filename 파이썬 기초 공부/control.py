a=input("봉사실적 입력 : ")
b=input("진로성적 입력 : ")

if(a.upper()=='P') and (b.upper()=='P'):
    print("매우 잘함")
elif (a.upper()=='P') or (b.upper()=='P'):
    print("잘함")
else :
    print("과락")