'''
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len: str = ""
        lista: list = []
        lista2: list = []
        if len(s) == 1: # If the string has only one character, it's already a palindrome
                return s
        for e in range(len(s)): # Outer loop to iterate through each character in the string
            for j in range(e, len(s)): # Inner loop to check all substrings starting from index 'e'
                # Add current character to both lists
                lista.append(s[j])
                lista2.append(s[j])
                # Reverse lista2 to compare with lista
                lista2.reverse() 
                if lista == lista2: # Check if the current substring is a palindrome
                    if len(lista) > len(max_len): # If the palindrome is longer than the current longest, update max_len
                        max_len = "".join(lista)
                lista2.reverse() # Restore lista2 to original order for next comparison
            # Reset lists for the next starting index 'e'
            lista = []
            lista2 = []
        return max_len
    

if __name__ == "__main__":
    
    sos = Solution()
    print(sos.longestPalindrome("jglknendplocymmvwtoxvebkekzfdhykknufqdkntnqvgfbahsljkobhbxkvyictzkqjqydczuxjkgecdyhixdttxfqmgksrkyvopwprsgoszftuhawflzjyuyrujrxluhzjvbflxgcovilthvuihzttzithnsqbdxtafxrfrblulsakrahulwthhbjcslceewxfxtavljpimaqqlcbrdgtgjryjytgxljxtravwdlnrrauxplempnbfeusgtqzjtzshwieutxdytlrrqvyemlyzolhbkzhyfyttevqnfvmpqjngcnazmaagwihxrhmcibyfkccyrqwnzlzqeuenhwlzhbxqxerfifzncimwqsfatudjihtumrtjtggzleovihifxufvwqeimbxvzlxwcsknksogsbwwdlwulnetdysvsfkonggeedtshxqkgbhoscjgpiel"))