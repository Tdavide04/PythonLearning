from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s2 = list(s2)
        k = len(s1)
        window = s2[:k]
        if Counter(s1) == Counter(window):
            return True
        for i in range(len(s2[k:])):
            window.pop(0)
            window.append(s2[i])
            if Counter(s1) == Counter(window):
                return True
        return False
    

sos = Solution()
print(sos.checkInclusion(s1="ab",s2="eidbaooo"))