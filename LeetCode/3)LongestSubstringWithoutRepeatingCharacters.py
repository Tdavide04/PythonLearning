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
        max_num = 0 # Variable to store the maximum length of substrings without repeating characters found so far.
        i = 0 # Index variable to iterate through the string 's'.
        while i < len(s):
            # If the current character is not in 'lista', it means no repetition within the current substring.
            if s[i] not in lista:
                lista.append(s[i]) # Add the current character to 'lista'.
                max_num = max(max_num, len(lista)) # Update 'max_num' with the maximum length found so far.
            else: 
                # If the current character is already in 'lista', remove characters from the start of 'lista'
                # until the duplicate character is removed, ensuring the substring remains unique.
                while s[i] in lista:
                    lista.pop(0)
                # After removing duplicates, add the current character to 'lista'.
                lista.append(s[i])
            i += 1
        return max_num
    
if __name__ == "__main__":
    
    sos = Solution()
    print(sos.lengthOfLongestSubstring("pwwkew"))