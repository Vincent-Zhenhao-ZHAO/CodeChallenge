intervals = [[1,4],[1,4]]
new_list = []
merge_list = []
second_list = []
first_list = []
count = 1
for i in range(len(intervals)):
    first_list = intervals[i]
    for j in range(i + 1,len(intervals)):
        second_list = intervals[j]
        if j > len(intervals) - 1:
            break
        if second_list[0] <= first_list[1]:
            if second_list[0] <= first_list[0]:
                merge_list = [second_list[0],second_list[1]]
                new_list.append(merge_list)
                break
            merge_list = [first_list[0],second_list[1]]
            new_list.append(merge_list)
            break
        if second_list[0] > first_list[1]:
            new_list.append(first_list)
            new_list.append(second_list)
            break
for k in new_list:
    if len(new_list) == 1:
        break
    for m in new_list[count:]:
        if k == m:
            new_list.remove(k)
            break
        if m[1] == k[1]:
            if m[0] < k[0]:
                new_list.remove(k)
                break
            else:
                if m in new_list:
                    new_list.remove(m)
                    break
    count += 1
print(new_list)


# intervals.sort(key=lambda x: x[0])

#         merged = []
#         for interval in intervals:
#             # if the list of merged intervals is empty or if the current
#             # interval does not overlap with the previous, simply append it.
#             if not merged or merged[-1][1] < interval[0]:
#                 merged.append(interval)
#             else:
#             # otherwise, there is overlap, so we merge the current and previous
#             # intervals.
#                 merged[-1][1] = max(merged[-1][1], interval[1])

#         return merged