

def maxProfit(prices) -> int:
    l, r = 0, 1
    maxProfit = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit, profit)
        else:
            l = r
        r += 1
    return maxProfit

def DynamicMaxProfit(prices):
    maxP = 0
    minBuy = prices[0]

    for sell in prices:
        maxP = max(maxP, sell - minBuy)
        minBuy = min(minBuy, sell)
    return maxP

print(maxProfit([10,1,5,6,7,1]))
print(DynamicMaxProfit([10,1,5,6,7,1]))