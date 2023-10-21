def maxProfit(prices):
    m = prices[0]
    profit = prices[0] - prices[0]
    if len(prices) > 1:
        for i in range(1, len(prices)):
            m = min(m, prices[i-1])
            if prices[i] - m > profit:
                profit = prices[i] - m
    return profit


print(maxProfit([2,4,1,10]))