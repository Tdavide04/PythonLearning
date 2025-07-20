'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        diz: dict = {}
        for e in s:
            if e in diz:
                diz[e] += 1
            else:
                diz[e] = 1
        for key, value in diz.items():
            if value == 1:
                return s.index(key)
        return -1
        
if __name__ == "__main__":
    
    sos = Solution()
    print(sos.firstUniqChar("loveleetcode"))