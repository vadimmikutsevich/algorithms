def makeGood(s: str) -> str:
    stack = []

    for i in range(len(s)):
        if stack and abs(ord(s[i]) - ord(stack[-1])) == 32:
            stack.pop()
        else:
            stack.append(s[i])

    return "".join(stack)


print(makeGood("leEeetcodDe"))
# Given a string s of lower and upper case English letters.

# A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where: