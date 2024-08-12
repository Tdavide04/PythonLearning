'''
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lista: list = []
        max_num = 0
        i = 0
        
        while i < len(s):
            
            if s[i] not in lista:
                lista.append(s[i])
            else:
                if len(lista) > max_num:
                    max_num = len(lista)
                lista = [s[i]]
            i += 1
        return max_num
        
    
    
if __name__ == "__main__":
    
    sos = Solution()
    print(sos.lengthOfLongestSubstring("pwwkew"))