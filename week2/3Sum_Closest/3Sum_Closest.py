# time limit problem
# def threeSumClosest(self, nums: List[int], target: int) -> int:
#     best_num = int()
#     best_gap = int()
#     first = True
#     for i in range(len(nums)-2):
#         for j in range(i+1,len(nums)-1):
#             for k in range(j+1,len(nums)):
#                 sum_num = nums[i] + nums[j] + nums[k]
#                 gap = abs(sum_num - target)
#                 if first:
#                     best_gap = gap
#                     best_num = sum_num
#                     first = False
#                     continue
#                 if gap < best_gap:
#                     best_num = sum_num
#                     best_gap = gap
#     return best_num

# improve:
# left-right pointer

# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         nums.sort()
#         best_gap = int()
#         first = True
#         best_sum = int()
#         for current in range(len(nums)-2):
#             left_pos = current + 1
#             right_pos = len(nums) - 1
#             while left_pos < len(nums) - 1 and right_pos > left_pos:
#                 sum_num = nums[current] + nums[left_pos] + nums[right_pos]
#                 gap = abs(sum_num - target)
#                 if sum_num > target:
#                     right_pos -= 1
#                 if sum_num == target:
#                     return sum_num
#                 if sum_num < target:
#                     left_pos += 1
#                 if first:
#                     best_gap = gap
#                     best_sum = sum_num
#                     first = False
#                     continue
#                 if gap < best_gap:
#                     best_sum = sum_num
#                     best_gap = gap
#                     continue
#         return best_sum
            