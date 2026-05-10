class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        k=[]
        m={}
        for item in strs:
            k.append("".join(sorted(item)))

        for item in k:
            i=0
            j=[]
            for item1 in strs:
                if item=="".join(sorted(item1)):
                    j.append(strs[i])
                i=i+1
            m[item]=j        
            
        final=[]
        for item in m:
            final.append(m[item])
        return final






            
        