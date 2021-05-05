# This is solution from textbook.

def longestPalindrome(s):
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left = left - 1
            right = right + 1
        return s[left+1:right]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''

    for i in range(len(s)-1):
        result = max(result,
                    expand(i, i+1),
                    expand(i, i+2),
                    key=len)

    return result

print(longestPalindrome('bababba'))
