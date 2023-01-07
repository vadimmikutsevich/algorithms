def maxNumberOfBalloons(text):
    hashMap = {
        "b": 0,
        "a": 0,
        "l": 0,
        "o": 0,
        "n": 0,
    }

    for i in range(len(text)):
        if text[i] in hashMap and text[i] == "l" or text[i] == "o":
            hashMap[text[i]] += 0.5
        elif text[i] in hashMap:
            hashMap[text[i]] += 1

    result = hashMap["b"]
    
    for x in hashMap:
        if hashMap[x] < result:
            result = hashMap[x]

    return int(result)

print(maxNumberOfBalloons("loonbalxballpoon"))
maxNumberOfBalloons("loonbalxballpoon")


# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
# You can use each character in text at most once. Return the maximum number of instances that can be formed.