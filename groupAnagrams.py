class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        p = []
        t = []
        for i in strs:
            sorted_str = ''.join(sorted(i))
            t.append(sorted_str)
        
        i = 0
        while i < len(strs):
            n = []
            start = 0
            while start < len(t):
                try:
                    index = t.index(t[i], start)
                    start = index + 1
                    n.append(strs[index])
                except ValueError:
                    break
            n.sort()
            if n not in p:
                p.append(n)
            i += 1
        return p