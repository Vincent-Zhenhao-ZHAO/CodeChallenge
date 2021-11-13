def Solution(S):
    def checkcurrent(S):
        capital = False
        currentlen = 0
        for count in range(0,len(S)):
            if S[count].isupper():
                capital = True
                currentlen += 1
            elif S[count].isdigit():
                if capital:
                    return currentlen,S[count:]
                elif count == 0:
                    return 0,S[count+1:]                  
                else:
                    return 0,S[count:]
            else:
                currentlen += 1
        if capital == False:
            return 0,S[count:]
        else:
            return currentlen,S[count:]
   
    max = -1
    slicedstring = S
    while slicedstring:
        if not len(slicedstring) ==1:
            current,slicedstring = checkcurrent(slicedstring) 
            if current != 0 and current > max:
                max = current
        else:
            if slicedstring.isupper():
                if max < 1:
                    max = 1
            slicedstring = ''


    return max

print(Solution('A0Ba'))