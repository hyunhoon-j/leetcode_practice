def reorderLogFiles(logs):
    letters = list()
    digits = list()

    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    #print(digits)
    #print(letters)

    letters.sort(key = lambda x: (x.split()[1:], x.split()[0]))

    return letters + digits

print(reorderLogFiles(["1 n u", "r 527", "j 893", "6 14", "6 82"]))
