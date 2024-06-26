class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            if((target - numbers[i]) in numbers):
                p = numbers.index(target - numbers[i])
                if(numbers[i] == numbers[p]):
                    p = p + 1
                return [i + 1, p + 1]