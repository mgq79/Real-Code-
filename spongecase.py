def spongecase(s):
    res = ""
    for i in range (len(s)):
        if s[i].isalpha():
            if (i%2 == 0):
                res += s[i].lower()
            else:
                res += s[i].upper()
        else:
            res += s[i]
    return res