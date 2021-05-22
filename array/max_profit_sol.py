import sys

def maxProfit(prices):
    # prices = [7, 1, 5, 3, 6, 4]
    profit = 0
    min_price = sys.maxsize # We need to set the min_price as high as possible to change the value to what we found from iteration

    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit

print(maxProfit([7, 1, 5, 3, 6, 4]))
# Answer: 5
