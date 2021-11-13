def Solution(S):
    def checkcurrent(S):
        capital = False
        currentlen = 0
        for character in S:
            if character.isupper():
                capital = True
                currentlen += 1
            elif character.isdigit():
                if capital:
                    return currentlen
                else:
                    return 0
            else:
                currentlen += 1
        if capital == False:
            return 0
        else:
            return currentlen
   
    max = -1
    for count in range(0,len(S)):
        if not S[count].isdigit():
            current = checkcurrent(S[count:]) 
            if current != 0 and current > max:
                max = current




    return max


print(Solution('a0bb'))