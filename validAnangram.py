class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        p = []
        l = []
        for i in s:
            p.append(i)
        for i in t:
            l.append(i)
        p.sort()
        l.sort()
        if(p==l):
            return True
        else:
            return False
        