# def twoSumLessThanK(self, nums: List[int], k: int) -> int:
#         nums = nums.sort()
#         max_num = -1
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 sum_num = nums[i] + nums[j]
#                 if sum_num > max_num and sum_num < k:
#                     max_num = sum_num
#         return max_num

# def twoSumLessThanK(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         max_num = -1
#         left_pointer = 0
#         right_pointer = len(nums) - 1
#         while left_pointer < right_pointer:
#             sum_num = nums[left_pointer] + nums[right_pointer]
#             if sum_num < k:
#                 max_num = max(max_num,sum_num)
#                 left_pointer += 1
#             else:
#                 right_pointer -= 1
#         return max_num