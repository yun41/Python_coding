def sort3(num1,num2,num3):
    list_num = []
    list_num.append(num1)
    list_num.append(num2)
    list_num.append(num3)
    list_num.sort()
    return list_num

print('세 수를 입력하세요 :')
num1 = int(input())
num2 = int(input())
num3 = int(input())
list_num = sort3(num1,num2,num3)
print('정렬된 리스트는 다음과 같습니다:',list_num[0],list_num[1],list_num[2])