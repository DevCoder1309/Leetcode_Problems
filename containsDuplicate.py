class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        print(nums)
        if(len(nums)==1):
            return False
        a = nums[0]
        for i in range(1 , len(nums)):
            if(a==nums[i]):
                return True
            else:
                a = nums[i]
        else:
            return False