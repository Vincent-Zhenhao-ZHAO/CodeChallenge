def solution(s):
    def checkset(input):
        if input == '(':
            return ')'
        elif input == '[':
            return ']'
        elif input == '{':
            return '}'
        else: 
            return False

    stack = []
    pt = -1
    setpointer = 0
    if len(s) % 2 != 0:
        return False
    for i in range(0,len(s)):
        if not stack or s[i] != setpointer:
            stack.append(s[i])
            pt += 1
            setpointer = checkset(s[i])
            if not setpointer:
                return False
        elif s[i] == setpointer:
            stack.pop()
            pt -= 1
            if pt != -1:
                setpointer = checkset(stack[pt])
            else:
                setpointer = 0
    if not stack:
        return True
    else:
        return False


print(solution("[([]])"))



   