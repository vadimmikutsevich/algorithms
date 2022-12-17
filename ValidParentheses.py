def isValid(s):
    stack = []
    mapOpen = {"(": "", "{": "", "[": ""}
    mapClosed = {")": "(", "}": "{", "]": "["}

    for i in range(len(s)):
        if s[i] in mapClosed and len(stack) > 0:
            if stack[len(stack)-1] == mapClosed[s[i]]:
                stack.pop(len(stack) - 1)
                continue
        stack.append(s[i])
        
    return not stack


print(isValid("]"))

# we must determine if the input string is valid 