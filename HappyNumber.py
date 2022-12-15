def isHappy(num):
    def recursionFunc(n):
        product = 0
        while n > 0:
            product += (n % 10) ** 2
            n = n // 10
        return product
    
    slow_runner = num
    fast_runner = recursionFunc(num)
    while fast_runner != 1 and fast_runner != slow_runner:
        slow_runner = recursionFunc(slow_runner)
        fast_runner = recursionFunc(recursionFunc(fast_runner))
    return fast_runner == 1
    

print(isHappy(1111111))

# in this case, we use Floyd's Cycle-Finding Algorithm to check happy number