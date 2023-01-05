def reverseString(s):
    j = len(s) - 1

    for i in range(len(s)):
        if j <= i: 
            print(s)
            return

        s[i], s[j] = s[j], s[i]
        j -= 1


reverseString(["H","a","n","n","a","h"])