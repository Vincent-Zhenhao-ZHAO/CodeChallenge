def solution(nums):
    maxlens = 0
    lens = 1
    myset = set(nums) 
    for i in myset:
        if ((i-1) not in myset):
            while (i + 1) in myset:
                lens += 1
                i += 1
        if lens > maxlens:
            maxlens = lens  
        lens = 1
             


    return maxlens

print(solution([9,1,-3,2,4,8,3,-1,6,-2,-4,7]))
