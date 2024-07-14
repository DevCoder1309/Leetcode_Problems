class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        c = []
        for i in range(len(nums) - 2):
            if(i > 0 and nums[i] == nums[i - 1]):
                continue
            target = nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[left] + nums[right]
                if sum == -target:
                    c.append([target, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  
                    left = left + 1
                    right = right - 1

                elif sum < -target:
                    left += 1
                else:
                    right -= 1

        return c