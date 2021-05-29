# Actually, this code exceeds the time limit for the test case from leetcode...

def groupAnagrams(strs):
    # Sort each word to make a norm
    word_srt_lst = [str(sorted(i)) for i in strs]

    # Make a set to make a frame of return value: [[], []...]
    tmp_set = set(word_srt_lst)

    new_lst = list()
    for i in range(len(tmp_set)):
        new_inner = list()
        new_lst.append(new_inner)

    clsf_lst = list(tmp_set)

    for i in range(len(clsf_lst)):
        for word in strs:
            if str(sorted(word)) == clsf_lst[i]:
                new_lst[i].append(word)

    return new_lst

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
