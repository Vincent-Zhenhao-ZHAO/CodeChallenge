a = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# set the boundary:
left = 0
right = len(a) - 1
# when goes to middle:
while left <= right:
    for i in range(right):
        top = left
        bottom = right
        top_left = a[top][left + i]
        a[top][left + i] = a[bottom - i][left]
        a[bottom - i][left] = a[bottom][right - i]
        a[bottom][right - i] = a[top + i][right]
        a[top + i][right] = top_left
        print(i,a)
    left += 1
    right -= 1
