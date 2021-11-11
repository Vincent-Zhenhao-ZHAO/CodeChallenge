# brute force
# for i in range (0,len(nums)):
#             for j in range (i+1,len(nums)):
#                 if nums[j] == target - nums[i]:
#                     return [i,j]
# nums = [3,2,3]
# target = 6
# restNum = target
# Target_NumList = []
# Target_OrdList = []
# for i in range(len(nums)):
#     restNum = restNum - nums[i]
#     nums = sorted(nums)
#     if restNum > 0:
#         Target_NumList.append(nums[i])
#         Target_OrdList.append(i)
#         continue
#     elif restNum < 0:
#         if i == 0:
#             Target_OrdList.remove(j)
#             Target_NumList.remove(nums[j])
#             continue
#         elif i != 0:
#             for j in range(0,i):
#                 if nums[j] > nums[i-1]:
#                     Target_OrdList.remove(j)
#                     Target_NumList.remove(nums[j])
#                     Target_OrdList.append(i)
#                     Target_NumList.append(nums[i])
#                     restNum = restNum + nums[j] 
#                     if restNum > 0:
#                         continue
#                     if restNum == 0:
#                         break
#                     if restNum != 0:
#                         continue
#             if restNum != 0:
#                 for k in range(i,len(nums)):
#                     pass
#             continue
#     elif restNum == 0:
#         Target_NumList.append(nums[i])
#         Target_OrdList.append(i)
#         break
# print(Target_NumList)
# use hashtable
# nums = [3,3]
# target = 6
# hashmap = {}  # use dictunary to apply hashtable
# for i in range(len(nums)):
#     hashmap[nums[i]] = i
# for i in range(len(nums)):
#     complement = target - nums[i]
#     if complement in hashmap and hashmap[complement] != i:
#         print([i, hashmap[complement]])