def max_profit(prices):
    if len(prices) < 2:
        return "Not enough data"

    min_price = prices[0]
    max_profit = prices[1] - prices[0]
    buy_day = 1
    sell_day = 2

    for i in range(1, len(prices)):
        if prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
            sell_day = i + 1
            buy_day = prices.index(min_price) + 1
        if prices[i] < min_price:
            min_price = prices[i]

    print("Day of buying :", buy_day)
    print("Day of Selling :", sell_day)

n = int(input())
prices = []
for _ in range(n):
    prices.append(int(input()))
max_profit(prices)
