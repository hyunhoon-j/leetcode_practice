def mostCommonWord(paragraph, banned):
    p = paragraph.lower()

    # Replace any sentence end mark into ''
    mark = ['.', ',', '?', '!', ';', ':', "'"]
    for i in mark:
        p = p.replace(i, ' ')

    # Split the string
    p = p.split()

    #print(p)

    if len(banned) != 0:
        for i in banned:
            print(i)
            while i in p:
                p.remove(i)

    #print(p)

    # Make a dictionary to find the most common word
    counts = dict()
    for elem in p:
        counts[elem] = counts.get(elem, 0) + 1

    bigword = None
    bigcount = None

    for word, count in counts.items():
        if bigcount is None or count > bigcount:
            bigcount = count
            bigword = word

    return bigword

print(mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]))
