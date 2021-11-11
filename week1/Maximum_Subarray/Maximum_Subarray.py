nums = [-2,-1]
# max_total = 0
# count = 0
# for each in nums:
#     if len(nums) == 1:
#         print(each)
#         break
#     if count == 0 and each < 0:
#         continue
#     if each < 0:
#         max_total = max_total + each
#         if max_total < 0 and max_total < each:
#             max_total = each
#             continue
#         max_total = max_total - each
#     max_total = each + max_total
#     if max_total < 0:
#         max_total = max_total - each
#         continue
#     count = 1
# print(max_total)
max_total = nums[0]
total = 0
for each in nums:
    if total < 0:
        total = 0
    total = total + each
    max_total = max(total,max_total)
print(max_total)
