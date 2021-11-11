# class Solution:
#     def lastStoneWeight(self, stones: List[int]) -> int:
#         def findSolution(stones):
#             if len(stones) == 0:
#                 return 0
#             if len(stones) == 1:
#                 return stones[0]
#             stones = sorted(stones,reverse=True)
#             first_stone = stones[0]
#             second_stone = stones[1]
#             if first_stone == second_stone:
#                 return findSolution(stones[2:])
#             if first_stone != second_stone:
#                 new_stone = first_stone - second_stone
#                 stones.append(new_stone)
#                 return findSolution(stones[2:])
#         return findSolution(stones)