def isPalindrome(s: str) -> bool:
    s = s.lower()

    new_s = str()
    for letter in s:
        if letter.isalnum():
            new_s = new_s + letter

    new_lst = [letter for letter in new_s]

    return new_lst == new_lst[::-1]

print(isPalindrome('race a car'))
