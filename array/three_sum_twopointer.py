# nums = [-1,0,1,2,-1,-4]

def threeSum(nums):
    results = list()
    # Sort numbers in a list
    nums.sort()
    # A result of the sorted nums in here: [-4, -1, -1, 0, 1, 2]

    for i in range(len(nums) - 2):
        # Skip the duplicated number
        if i > 0 and nums[i] == nums[i-1]:
            continue

        # Two pointer
        # Make indices
        left = i + 1
        right = len(nums) - 1

        # Control the movement of each pointer
        while left < right:
            # Check sum
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left = left + 1
            elif sum > 0:
                right = right - 1
            else:
                results.append([nums[i], nums[left], nums[right]])

                # Skip the duplicated number because the number is already used.
                while left < right and nums[left] == nums[left+1]:
                    left = left + 1
                while left < right and nums[right] == nums[right-1]:
                    right = right - 1

                # Set the next indices
                left = left + 1
                right = right - 1

    return results

print(threeSum([-1,0,1,2,-1,-4]))
