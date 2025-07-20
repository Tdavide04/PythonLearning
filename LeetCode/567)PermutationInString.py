'''
Given two strings s1 and s2, return true if s2 contains a
permutation
of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

 

Constraints:

    1 <= s1.length, s2.length <= 104
    s1 and s2 consist of lowercase English letters.
'''

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s2 = list(s2)
        k = len(s1)
        window = s2[:k]
        if Counter(s1) == Counter(window):
            return True
        s2 = s2[k:]
        for i in range(len(s2)):
            window.pop(0)
            window.append(s2[i])
            if Counter(s1) == Counter(window):
                return True
        return False 
    

if __name__ == "__main__":
    
    sos = Solution()
    print(sos.checkInclusion(s1="abc",s2="bbbca"))