# even_odd = lambda num : "Even" if num%2==0 else "Odd"
# print(even_odd(3))


# x = int(input("수를 입력하세요: "))

# for i in range(1,10):
#     multi = lambda x : x*i
#     print("{0} X {1} = {2}".format(x,i,multi(x)))

# def func1(numbers):
#     result = []
#     for number in numbers:
#         if number >= 10:
#             result.append(number)
#     return result

# print(func1([9,10,11,12,13,14]))


func1 = lambda numbers : [number for number in numbers if number >= 10]
print(func1([9,10,11,12,13,14]))