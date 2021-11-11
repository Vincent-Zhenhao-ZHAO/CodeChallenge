nums1 = [1,3]
nums2 = [2,7]
length_nums1 = len(nums1)
length_nums2 = len(nums2)
merge_list = []
long_list = []
short_list = []
if length_nums1 > length_nums2:
    short_list = nums2
    long_list = nums1
elif length_nums2 > length_nums1:
    short_list = nums1
    long_list = nums2
else:
    short_list = nums1
    long_list = nums2
for i in range(len(short_list)):
    for j in range(len(long_list)):
        if short_list[i] < long_list[j]:
            if j < 1:
                merge_list.append(short_list[i])
                continue
        if short_list[i] > long_list[j]:
            if j in merge_list:
                continue
            merge_list.append(long_list[j])
            continue
        if short_list[i] == long_list[j]:
            if i in merge_list:
                continue
            merge_list.append(short_list[i])
            continue
for k in range(0,len(long_list)):
    if long_list[k] not in merge_list:
        merge_list.append(long_list[k])
print(merge_list)