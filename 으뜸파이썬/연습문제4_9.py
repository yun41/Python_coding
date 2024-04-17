def mean_of_n(nums):
    sum_num = 0
    for num in nums:
        sum_num += num
    mean_num = sum_num / len(nums)
    return mean_num

def max_of_n(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
    max_num = nums[len(nums)-1]
    return max_num

def min_of_n(nums):
    for j in range(len(nums)-1):
        if nums[j] < nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
    min_num = nums[len(nums)-1]
    return min_num

list_num = list(map(int, input('정수를 여러 개 입력하시오 : ').split()))
print('평균값은 {:.1f}'.format(mean_of_n(list_num)))
print('최댓값은',max_of_n(list_num))
print('최솟값은',min_of_n(list_num))
