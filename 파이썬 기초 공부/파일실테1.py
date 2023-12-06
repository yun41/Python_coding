#input1=int(input("첫 번째 숫자를 입력하세요. "))
#input2=int(input("두 번째 숫자를 입력하세요. "))
#
#total = input1 + input2
#print("두 수의 합은 %s 입니다" %total)

# input_numbers = input("숫자를 입력하시오. ")
# numbers=input_numbers.split(",")
# sum=0

# print(numbers)
# for num in numbers:
#     sum+=int(num)
# print(sum)

# number = int(input("구구단을 출력할 숫자(2~9): "))
# for i in range(1,10):
#     print(number*i,end=" ")

# with open("t1.txt",'w') as f1:
#     f1.write("Experience is valuable!")

# with open("t1.txt",'r') as f2:
#     print(f2.read())

with open("t2.txt", 'w') as t2:
    t2.write(input("저장할 내용을 입력하세요: "))

with open("t2.txt") as t1:
    print(t1.read())