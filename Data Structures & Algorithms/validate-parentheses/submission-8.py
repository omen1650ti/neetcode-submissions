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
                print("hi")
                se.append(characters)
                print(se)
            else:
                if len(se)==0:
                    return False
                k=se.pop()
                print(characters)
                if h[k]!=characters:
                    return False
        print(se)
        if len(se) == 0:
            return True
        else:
            return False
        