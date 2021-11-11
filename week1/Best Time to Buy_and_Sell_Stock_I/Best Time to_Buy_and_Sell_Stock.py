# return date
# prices = [1,2,4]
# hashtable1 = {}
# hashtable2 = {}
# profit = 0
# for i in range(len(prices)):
#     hashtable1[prices[i]] = i + 1
# for i in range(len(prices)):
#     hashtable2[i+1] = prices[i]
# sorted_price = prices
# sorted_price.sort()
# low_price = sorted_price[0]
# max_index = hashtable1[low_price] - 1
# sall_day = -2
# sall_price = 0
# count = 0
# for j in hashtable1.values():
#     if count > max_index:
#         price = hashtable2[j]
#         if price > low_price:
#             sall_price = hashtable1[price]
#             profit = sall_price - low_price
#             continue
#     count += 1
# if profit < 0:
#     print(0)
# print(profit)
#  return profit
prices = [7,1,5,3,6,4]
profit = 0
max_profit = 0
k = 1
for i in prices:
    for j in prices[k:]:
        profit = j - i
        if profit > max_profit:
            max_profit = profit
    k += 1
print(max_profit) 

# profit = 0
# lowest_buy = prices[0]

# for price in prices[1:]:
#     if price < lowest_buy:
#         lowest_buy = price
#     else:
#         profit = max(profit, price - lowest_buy)
        
# return profit