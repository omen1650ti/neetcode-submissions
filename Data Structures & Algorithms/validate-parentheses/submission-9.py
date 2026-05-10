class Solution:
    def isValid(self, s: str) -> bool:
        h={
            "{": "}",
            "(":")",
            "[":"]"
        }

        se=[]

        for characters in s:
            if characters not in [")", "]", "}"]:
                
                se.append(characters)
                
            else:
                if len(se)==0:
                    return False
                k=se.pop()
                
                if h[k]!=characters:
                    return False
        
        if len(se) == 0:
            return True
        else:
            return False
        