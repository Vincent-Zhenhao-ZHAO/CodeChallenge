def solution(inputarray):
    currentmax = 0
    maxarea = 0
    currentarea1 = 0
    currentarea2 =  0
    pointer1 = 0
    pointer2 = len(inputarray)-1
    while pointer1 != pointer2 and pointer1 < len(inputarray):
        currentarea1 = (pointer2 - pointer1) * min(inputarray[pointer2],inputarray[pointer1])
        if currentarea1 > maxarea:
            maxarea = currentarea1
        if inputarray[pointer1] > inputarray[pointer2]:
            pointer2 -= 1
        else:
            pointer1 += 1
        
    


    return maxarea

print(solution([1,8,6,2,5,4,8,3,7]))