def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []


nums = [2, 5, 8, 6]
target = 13

output = twoSum(nums, target)
print(output)
