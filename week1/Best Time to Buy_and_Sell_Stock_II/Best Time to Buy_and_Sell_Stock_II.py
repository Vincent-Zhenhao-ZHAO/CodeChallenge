prices = [1,2,3,4,5]
low_price = -1
profit = 0
total_profit = 0
next_price = 0
for date in range(len(prices)):
    day_price = prices[date]
    if date+1 <= len(prices) -1 :
        next_price = prices[date + 1]
    if day_price >= next_price:
        if low_price != -1:
            profit = day_price - low_price
            total_profit = profit + total_profit
            low_price = -1
        continue
    elif day_price < next_price:
        if low_price != -1:
            profit = day_price - low_price
            total_profit = profit + total_profit
            low_price = -1
        low_price = day_price
        continue
print(total_profit)