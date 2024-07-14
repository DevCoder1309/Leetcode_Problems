class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        p = []
        if(len(nums)==1 and nums[0]==target):
            return p.append(0)
        j = 0
        d = 0
        i = 1
        while(d != len(nums) - 1 and j < len(nums) and i < len(nums)):
            if(nums[j] + nums[i] == target):
                p.append(j)
                p.append(i)
                return p
            elif(nums[i] == nums[len(nums) - 1] and i == len(nums) - 1):
                d = 0
                j = j + 1
                i = j
            i = i + 1
            d = d + 1
            