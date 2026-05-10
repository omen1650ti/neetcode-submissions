class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n={}
        u=[]
        for item in nums:
            if item not in u:
                u.append(item)
        for item in u:
            i=1
            for item1 in nums:
                if item==item1:
                    n[item]=i 
                    i=i+1

        sorted_dict = dict(sorted(n.items(), key=lambda x: x[1], reverse=True))
        count=1
        fin=[]
        for key,values in sorted_dict.items():
            if count<=k:
                fin.append(key)
                count=count+1
        return fin
            
        