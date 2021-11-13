def searchInsert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def recursion(nums, target):
            halfpoint = len(nums)//2
            if target < nums[0]:
                return nums[0]
            elif target > nums[len(nums)-1]:
                return nums[len(nums)-1]
            elif target == nums[halfpoint]:
                return nums[halfpoint]
            elif target >= nums[halfpoint]:
                return recursion(nums[halfpoint:], target)
            elif target <= nums[halfpoint]:
                return recursion(nums[:halfpoint], target)
        value = recursion(nums,target)
        index = nums.index(value)
        if value == target or target < value:
            return index
        else:
            return index + 1
        
        



print(searchInsert([1,3,5,6],5))