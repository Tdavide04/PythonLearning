'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. 
In this scenario, how would you change your code?
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: # If the string 's' is empty, it is trivially a subsequence of any string, including 't'.
            return True
        count = 0
        for char in s: 
            if char in t: # Check if the current character from 's' exists in the string 't'.
                count += 1
                # Update 't' by removing the part up to and including the current character.
                # This is done to ensure that the next match only considers the remaining substring of 't'.
                t = t[t.index(char) + 1:]
            if count == len(s): # If the count equals the length of 's', it means all characters in 's' have been matched in sequence.
                return True
        return False
                
                
    
if __name__ == "__main__":
    
    sos = Solution()
    print(sos.isSubsequence(s ="acb", t = "ahbgdc"))