def my_sort(*nums):
    list_nums = []
    for n in nums:
        list_nums.append(n)
    list_nums.sort()
    print('결과 :',list_nums)

my_sort(45,3,4,56,5)
my_sort(9,8,7,6,5,4,3)