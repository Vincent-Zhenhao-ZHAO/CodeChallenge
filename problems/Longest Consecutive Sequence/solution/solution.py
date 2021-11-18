def solution(nums):


    #maximum = max(nums)
    lens = 1
    maxlen = 0
    
    
    while nums:
        current = min(nums)
        finished = False
        while not finished:
            if (current+1) in nums:
                nums.remove(current)
                lens += 1
                current += 1
            else:
                if maxlen < lens:
                    maxlen = lens
                lens = 1
                finished = True
                nums.remove(current)
            
    return maxlen


print(solution([9,1,-3,2,4,8,3,-1,6,-2,-4,7]))
