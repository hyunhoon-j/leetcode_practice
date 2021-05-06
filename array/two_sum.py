nums = [2, 7, 11, 15, 19]
target = 9

# brute force algorithm

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print(i, j)

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

print(twoSum([2, 7, 11, 15, 19], 9))
