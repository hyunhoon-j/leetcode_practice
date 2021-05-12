# Timeout...

def threeSum(nums):
    if len(nums) == 0:
        return []
    elif len(nums) == 1 and nums[0] == 0:
        return []

    tmp_lst = list()

    # Brute force algorithm
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    tmp_lst.append([nums[i], nums[j], nums[k]])

    fin_lst = list()

    for elem in tmp_lst:
        fin_lst.append(sorted(elem))

    res = list()

    for elem in fin_lst:
        if elem not in res:
            res.append(elem)

    return res
