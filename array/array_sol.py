# nums = [6,2,6,5,1,2]

def arrayPairSum(nums):
    sum = 0
    pair = list() # We are going to focus on only one pair composed of the numbers from the sorted list
    nums.sort() # [1, 2, 2, 5, 6, 6]

    for n in nums:
        pair.append(n)
        if len(pair) == 2: # Focus on just two numbers because we can get the max value from the min value of that numbers
            sum = sum + min(pair)
            pair = list()

    return sum

print(arrayPairSum([6,2,6,5,1,2]))
# Answer: 9
