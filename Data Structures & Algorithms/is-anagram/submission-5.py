class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist = sorted(list(s))
        tlist = sorted(list(t))
        for i in range(len(s)):
            if slist[i] != tlist[i] or len(slist) != len(tlist):
                return False
        return True