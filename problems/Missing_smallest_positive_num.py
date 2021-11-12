def solution(A):
    # write your code in Python 3.6
    #remove any repetation
    A = list(dict.fromkeys(A))
    #sort the array? O(nlogn)
    A.sort()
    #check if all the numbers are negative, if yes then return 1
    if max(A) <= 0:
        return 1
        #Conditions left are ones that containing values > 1
        #First way: loop from 1 until the maximum number and return the value that is not in the list O(n)
    else:
        #remove all the negative numbers in the list
        A = [x for x in A if x > 0]
        for i in range(0,max(A)):
            if (i+1) != A[i]:
                return (i+1)
        #If the sequence of numbers does not have a gap, then return value that's 1 greater than max(A)
        return max(A)+1
    pass


print(solution([-2,5,7,23,567,123,45,6,9,8,10,50,20,11,1,2,3,4,5,6,7,8]))
