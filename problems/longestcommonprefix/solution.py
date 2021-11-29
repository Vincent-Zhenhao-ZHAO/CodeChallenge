def solution(strs):
    common = ""
    x = min(strs, key=len)
    for pointer in range(0,len(x)):
        for y in strs:
            if not (x[pointer] ==  y[pointer]):
                return common
        common = common + y[pointer]


print(solution(["flower","flow","flight"]))