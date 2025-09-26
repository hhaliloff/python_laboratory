nums = [1, 7, 8, 15]
target = 9

def two_sum(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if not((type(nums[i]) == int or type(nums[i]) == float) and (type(nums[j]) == int or type(nums[j]) == float)):
                return 'Ошибка. Пожалуйста, введите числа'
            elif nums[i] + nums[j] == target:
                res = [i, j]
                return res
    return None

print(two_sum(nums, target))