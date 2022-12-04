def subtractProductAndSum(n):
    sum = 0
    product = 1

    while n != 0:
        sum = sum + n % 10
        product = product * (n % 10)
        n = n // 10

    return product - sum

subtractProductAndSum(234)

# we expect the difference between the product of its digits and the sum of its digits