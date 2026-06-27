"""
Concept:
The Best Time to Buy and Sell Stock problem finds the maximum profit that can
be earned by buying one stock and selling it later.

Profit = Selling Price - Buying Price

Example:
Prices = [7, 2, 1, 5, 6, 4, 8]

Buy at 1
Sell at 8

Maximum Profit = 7

Program: Best Time to Buy and Sell Stock
Description:
    Method 1: Brute Force by checking every buy-sell pair.
    Method 2: Track the minimum price and maximum profit.
    Method 3: Track buy price, sell price and maximum profit.
Complexity:
    Method 1: Time O(n²) | Space O(1)
    Method 2: Time O(n) | Space O(1)
    Method 3: Time O(n) | Space O(1)
"""

# Method 1: Brute Force
prices = [7, 2, 1, 5, 6, 4, 8]

n = len(prices)

max_profit = 0

for i in range(n):
    for j in range(i + 1, n):
        if prices[j] > prices[i]:
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)

print(max_profit)


# Method 2: Track minimum price
prices = [7, 2, 1, 5, 6, 4, 8]

n = len(prices)

max_profit = 0
min_price = float("inf")

for i in range(n):

    min_price = min(min_price, prices[i])

    max_profit = max(max_profit, prices[i] - min_price)

print(max_profit)


# Method 3: Track buy and sell prices
prices = [7, 2, 1, 5, 6, 4, 8]

n = len(prices)

max_profit = 0
min_price = float("inf")

buy_price = 0
sell_price = 0

for i in range(n):

    if prices[i] < min_price:
        min_price = prices[i]
        buy_price = prices[i]

    if prices[i] - min_price > max_profit:
        max_profit = prices[i] - min_price
        sell_price = prices[i]

print(f"Buy at {buy_price}")
print(f"Sell at {sell_price}")
print(f"Profit = {max_profit}")


# Method 1 output :
# 7

# Method 2 output :
# 7

# Method 3 output :
# Buy at 1
# Sell at 8
# Profit = 7

