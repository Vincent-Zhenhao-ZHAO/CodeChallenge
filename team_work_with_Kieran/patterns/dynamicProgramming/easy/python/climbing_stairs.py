# leetcode Q70
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# think with connection with Fibonacci num

# this method used the dfs search to find the solution, in this question, draw the tree
# then you will find the longest tree is what we need, then use it to solve the problem

def climbing_stairs(n):

    cache = {}

    def climb(x):

        if x in cache:
            pass

        if x == 0 or x == 1:
            cache[x] = 1

        else:
            cache[x] = climb(x - 1) + climb(x - 2)

        return cache[x]

    return climb(n)


print(climbing_stairs(38))

# n = 5
# if n == 1:
#     print(1)
# dfs = []
# dfs.append(1)
# dfs.append(2)
# i = 2
# while i < n:
#     dfs.append(0)
#     dfs[i] = dfs[i-1] + dfs[i-2]
#     i = i + 1
# print(dfs[n-1])
