'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels: str = "aeiouAEIOU" # Define a string containing all the vowels (both lowercase and uppercase)
        temporary_list: list = []
        for e in s:
            if e in vowels: # If the current character is a vowel, add it to the temporary list
                temporary_list.append(e) 
        temporary_list.reverse()
        s:list = list(s) # Convert the input string 's' to a list so that we can modify it (since strings are immutable in Python)
        for e in range(len(s)):
            if s[e] in vowels: # If the current character in 's' is a vowel
                s[e] = temporary_list[0] # Replace it with the first vowel from the reversed temporary list
                temporary_list.pop(0)
        return "".join(s)
    
    
if __name__ == "__main__":
    
    sos = Solution()
    print(sos.reverseVowels(s = "leetcode"))