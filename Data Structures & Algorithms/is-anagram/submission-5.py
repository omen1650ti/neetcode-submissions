class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        slist=list(s)
        tlist=list(t)
        slist.sort()
        tlist.sort()
        s1="".join(slist)
        t1="".join(tlist)
        if s1==t1:
            return True
        else:
            return False
        # for i in range(0,len(slist)):
        #     if slist[i] != tlist[i]:
        #         return False
        # return True
        