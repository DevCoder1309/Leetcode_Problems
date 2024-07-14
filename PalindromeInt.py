class Solution:
    def isPalindrome(self, x: int) -> bool:
        j = str(x)
        w = []
        for i in range(len(j)-1,-1,-1):
            w.append(j[i])
        c = ''.join(w)
        if c==j:
            return True
        else:
            return False