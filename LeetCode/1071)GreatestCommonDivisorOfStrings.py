'''
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
'''

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        common_prefix = ""
        min_len = min(len(str1), len(str2)) # Find the length of the shorter string between str1 and str2
        
        # Find the common prefix between the two strings
        for e in range(min_len):
            if str1[e] == str2[e]:  # If characters match at the current index
                common_prefix += str1[e]  # Add to the common prefix
            else:
                break  # Stop if characters don't match
        
        # We iterate from the length of common_prefix down to 1 (from the longest possible prefix to the shortest).
        for i in range(len(common_prefix), 0, -1): 
            candidate = common_prefix[:i]  # Extract the prefix of length i from common_prefix
            # We use replace to remove all occurrences of candidate from both str1 and str2. 
            # If the resulting strings are empty, it means candidate is a valid divisor for both strings.
            if str1.replace(candidate, "") == "" and str2.replace(candidate, "") == "":
                return candidate  # If true, return candidate as it is the longest common divisor
        
        # If no valid prefix found that can divide both str1 and str2, return an empty string
        return ""
    
if __name__ == "__main__":
    
    sos = Solution()
    print(sos.gcdOfStrings(str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX", str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))