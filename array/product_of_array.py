# Timeout...

nums = [-1,1,0,-3,3]
nums = tuple(nums)

fin_lst = list()

for i in range(len(nums)):
    nums_tmp = list(nums)
    nums_tmp.remove(nums[i])

    tmp_str = None
    for num in nums_tmp:
        if tmp_str == None:
            tmp_str = num
        else:
            tmp_str = tmp_str * num

    fin_lst.append(tmp_str)

print(fin_lst)
