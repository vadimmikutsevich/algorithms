def canConstruct(ransomNote, magazine):
    hashMap = {}

    for i in range(len(magazine)):
        if magazine[i] in hashMap:
            hashMap[magazine[i]] += 1
        else:
            hashMap[magazine[i]] = 1

    for j in range(len(ransomNote)):
        if ransomNote[j] in hashMap and hashMap[ransomNote[j]] <= 0:
            return False
        elif ransomNote[j] in hashMap and hashMap[ransomNote[j]] > 0:
            hashMap[ransomNote[j]] -= 1
        elif ransomNote[j] not in hashMap:
            return False

    return True

canConstruct("aa", "aab")


# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.