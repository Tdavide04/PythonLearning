'''
Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

if no such substring exists, return 0.

 

Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
 

Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 105
'''

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        max_len: int = 0
        left: int = 0
        diz = {}
        for right in s:
            if right in diz:
                diz[right] +=1
            else:
                diz[right] = 1
                 

if __name__ == "__main__":
    
    sos = Solution()
    print(sos.longestSubstring())
    print(sos.longestSubstring())
    print(sos.longestSubstring())
    print(sos.longestSubstring())
    print(sos.longestSubstring())