class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        v=list(s)
        v1=list(t)
        v.sort()
        v1.sort()
        print(v)
        print(v1)
        i = 0
        j=0

        if len(v) == len(v1):
            while i < len(v):
                if v[i] == v1[j]:
                    i=i+1
                    j=j+1
                else:
                    return False
            return True


        else:
            return False
        