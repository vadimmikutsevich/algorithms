def сountOddNumbers(low, high):
    if low % 2 == 0:
      return (high-low+1)//2
    return (high-low)//2 + 1

сountOddNumbers(0, 10)

# we expect count of odd numbers