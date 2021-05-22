# Timeout...
def maxProfit(prices):
    # prices = [2, 1, 4]
    profit = 0

    # Brute force algorithm
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]

    if profit >= 0:
        return profit
    else:
        return 0

print(maxProfit([2, 1, 4]))
# Answer: 3
