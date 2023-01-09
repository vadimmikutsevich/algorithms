def lengthOfLongestSubstring(s: str) -> int:
    answer = start = 0
    hashMap = {}

    for i in range(len(s)):
        if s[i] in hashMap:
            start = max(start, hashMap[s[i]])
        hashMap[s[i]] = i + 1
        answer = max(answer, i - start + 1)

    return answer

lengthOfLongestSubstring("pwwkew")

# Given a string s, find the length of the longest substring without repeating characters.