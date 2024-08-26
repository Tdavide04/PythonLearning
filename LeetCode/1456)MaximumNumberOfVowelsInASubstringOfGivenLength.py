'''
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length
'''

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiouAEIOU" # Define the set of vowels for easy lookup
        # Initialize the current count of vowels in the initial window
        current_counter = 0
        max_counter = 0
        # Calculate the number of vowels in the first window of length k
        for i in range(k):
            if s[i] in vowels:
                current_counter += 1
        # Set the maximum count to the initial window's vowel count
        max_counter = current_counter
        # Slide the window across the string from index k to the end
        for i in range(k, len(s)):
            # Add the new character to the window (right side)
            if s[i] in vowels:
                current_counter += 1
            # Remove the character that falls out of the window (left side)
            if s[i - k] in vowels:
                current_counter -= 1
            # Update the maximum vowel count found so far
            max_counter = max(max_counter, current_counter)
        return max_counter
            
            
    
if __name__ == "__main__":
    
    sos = Solution()
    print(sos.maxVowels(s = "weallloveyou", k = 7))
    print(sos.maxVowels(s = "abciiidef", k = 3))