def firstUniqChar(s):
    visited = []

    for i in range(len(s)):
        if s[i] in visited:
            continue
        else:
            if s[i] not in s[i+1:]:
                return i
                break
    return -1

print(firstUniqChar("leetcode"))

# find the first non-repeating character in it and return its index. If it does not exist, return -1.