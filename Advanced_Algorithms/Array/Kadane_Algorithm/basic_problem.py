# Find a non-empty subarray with the largest sum.
# Example: [4,-1,2,-7,3,4]

# O(n^2)
def bruteForce(arr):
    
    if arr == []:
        return -1
    
    maxSum = arr[0]
    
    for i in range(len(arr)):
        currentSum = 0
        for j in range(i,len(arr)):
            currentSum += arr[j]
            maxSum = max(maxSum,currentSum)
            
    return maxSum

def kadanes(arr):
    
    if arr == []:
        return -1
    
    maxSum = arr[0]
    currentSum = 0
    
    for each in arr:
        currentSum = max(currentSum,0)
        currentSum += each
        maxSum = max(maxSum,currentSum)
        
    return maxSum

def test_answer():
    assert bruteForce([]) == -1
    assert bruteForce([4,-1,2,-7,3,4]) == 7
    print("Brute force solution Pass all the test")
    assert kadanes([]) == -1
    assert kadanes([4,-1,2,-7,3,4]) == 7
    print("kadanes solution Pass all the test")
    
test_answer()