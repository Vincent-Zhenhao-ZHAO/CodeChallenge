def solution(s):
    def checker(mystr):
        currentlen = 0
        table = []
        for i in mystr:
            if i not in table:
                table.append(i)
                currentlen += 1
            else: 
                return currentlen
        return currentlen

    
    uniqtable = []
    maxlen = 0
    if len(s) == 0:
        return 0
    else:
        while s and len(s) > maxlen:
            length = checker(s)
            if length > maxlen:
                maxlen = length
                s = s[1:]
            elif len(s) != 1:
                s = s[1:]
            else: 
                return maxlen


    return maxlen

print(solution('abcabcbb'))