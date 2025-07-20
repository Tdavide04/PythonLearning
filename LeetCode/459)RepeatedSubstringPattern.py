'''
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
'''

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Get the length of the input string.
        n = len(s)
        
        # Iterate over possible lengths of the substring, ranging from 1 to half the length of the string.
        # We only need to check up to half the string's length because any repeating pattern must be 
        # a divisor of the string length.
        for i in range(1, n // 2 + 1):
            # Check if the current length 'i' is a divisor of the string length 'n'.
            # If it is, then 's' might be made up of a repeated substring of this length.
            if n % i == 0:
                # Extract the potential repeating substring of length 'i'.
                substring = s[:i]
                
                # Multiply this substring by the number of times it should repeat to match the length of 's'.
                # Compare the result with the original string.
                if substring * (n // i) == s:
                    # If the constructed string matches the original, return True, indicating that 's' is
                    # made up of a repeated substring pattern.
                    return True
        
        # If no valid repeating pattern is found, return False.
        return False

    
if __name__ == "__main__":
    
    sos = Solution()
    print(sos.repeatedSubstringPattern("abcabcabcabc"))