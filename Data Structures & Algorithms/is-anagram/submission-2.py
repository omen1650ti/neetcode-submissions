class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=list(s)
        t1=list(t)
        s1.sort()
        t1.sort()
        s2="".join(s1)
        t2="".join(t1)
        if s2==t2:
            return True
        else:
            return False
       