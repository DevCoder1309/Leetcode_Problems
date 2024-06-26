class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l = []
        if(len(nums) == 0):
            return 0
        if(len(nums) == 1):
            return 1
        nums.sort()
        p = nums[0]
        t = [0]
        for i in range(1, len(nums)):
            if(nums[i] == p + 1):
                l.append(p)
                p = nums[i]
                t.append(len(l))
            elif(nums[i] == p):
                continue
            else:
                l = []
                p = nums[i]
        return max(t) + 1