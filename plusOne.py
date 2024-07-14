class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        b = []
        for i in range(len(digits)):
            b.append(str(digits[i]))

        c = ''.join(b)
        c = int(c)
        c = c + 1
        c = str(c)
        b = []
        for i in range(len(c)):
            b.append(int(c[i]))

        return b
        