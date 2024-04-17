list_n = list(map(int, input('여러 개의 정수를 입력하세요: ').split()))
print('합 :',sum(list_n))
mean = sum(list_n)/len(list_n)
print('평균 :',mean)

for i in range(len(list_n)):
    list_n[i] = ((list_n[i]-mean)**2)

standard_ = (sum(list_n)/len(list_n))**(1/2)
print('표준편차 : {:.2f}'.format(standard_))