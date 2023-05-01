class Solution:
    def romanToInt(self, s: str) -> int:
        ankit = {"I":1,
             "V":5,
             "X":10,
             "L":50,
             "C":100,
             "D":500,
             "M":1000}
        w = 0
        for i in range(len(s)-1):
            if ankit[s[i+1]]>ankit[s[i]]:
                w = w - ankit[s[i]]
            else:
                w = w + ankit[s[i]]
        w = w + ankit[s[len(s)-1]]
        return w
