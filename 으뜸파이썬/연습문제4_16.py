inputList = list(map(int,input('쉼표로 구분된 정수를 여러 개 입력하시오: ').split(',')))

print('입력된 정수의 리스트:',inputList)
print('정렬된 정수의 리스트: ',end='')
inputList.sort()
for i in range(len(inputList)):
    n=inputList[i]
    print(n,end=' ')