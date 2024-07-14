class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(e for e in s if e.isalnum()).lower()
        a = ''
        b = []
        for i in range(len(s) - 1, -1, -1):
            b.append(s[i])
        a = ''.join(b)
        if(a == s):
            return True
        else:
            return False


        