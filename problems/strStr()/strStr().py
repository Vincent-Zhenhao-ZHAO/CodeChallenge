def solution(haystack,needle):
    length = len(needle)
    needleindex = -1
    found = True
    if len(haystack) == 0 and len(needle) == 0:
        return 0
    elif len(haystack) == 0:
        return needleindex
    elif len(needle) == 0:
        return 0
    for count in range(0,len(haystack)):
        current = haystack[count:(count+length)]
        found = True
        if current != needle:
            found = False
        if found:
            needleindex = count
            break
        

                
                
            
    return needleindex

print(solution("apple","ll"))