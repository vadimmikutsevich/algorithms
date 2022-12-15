def maxProfit(prices):
    if len(prices) <= 1:
        return 0

    minValue = prices[0]
    profit = 0

    for i in range(len(prices)):
        if prices[i] < minValue:
            minValue = prices[i]
        elif prices[i] - minValue > profit:
            profit = prices[i] - minValue
        
    return profit

            

maxProfit([7,1,5,3,6,4])

# we need to get the best deal these days