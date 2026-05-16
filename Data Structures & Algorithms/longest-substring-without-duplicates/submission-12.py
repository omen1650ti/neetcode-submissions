class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k=[]
        i=0
        j=0
        max1=0
        while j>=i and j<len(s):

            if s[j] not in k:
                k.append(s[j])
                max1=max(max1,len(k)) 
                j=j+1
            else:
                max1=max(max1,len(k)) 
                k.remove(s[i])
                i += 1
            print(k)
        return max1
        