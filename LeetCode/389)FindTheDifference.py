'''
You are given two strings s and t.

String t is generated by random shuffling string s and then add one more letter at a random position.

Return the letter that was added to t.

 

Example 1:

Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.
Example 2:

Input: s = "", t = "y"
Output: "y"
 

Constraints:

0 <= s.length <= 1000
t.length == s.length + 1
s and t consist of lowercase English letters.
'''

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Check if the length of string 't' is greater than the length of string 's'.
        # This would indicate that 't' has one extra character compared to 's'.
        if len(t) > len(s):
            # Iterate over each character in string 't'.
            for i in t:
                # For each character, check if its count in 't' is greater than its count in 's'.
                # This will identify the extra character added to 't'.
                if t.count(i) > s.count(i):
                    # Return the extra character as the result.
                    return(i)

    

if __name__ == "__main__":
    
    sos = Solution()
    print(sos.findTheDifference(s = "abcd", t = "abcde"))