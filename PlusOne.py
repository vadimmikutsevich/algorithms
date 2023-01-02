def plusOne(digits):
    length = len(digits)

    for i in range(len(digits)):
        lastCurrent = length - i - 1
        
        if digits[lastCurrent] == 9:
           digits[lastCurrent] = 0
        else:
            digits[lastCurrent] += 1
            return 

    return [1] + digits

plusOne([4,3,9,9])

# it seems to be more than 1 (arr + 1)