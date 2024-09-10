'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
 

Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.
'''

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Initialize an empty dictionary to store character counts
        diz: dict = {}
        # Iterate over each character in the input string 'text'
        for e in text:
            # Increment the count of the character 'e' in the dictionary
            # If 'e' is not in the dictionary, use get() to return 0 and start counting from 1
            diz[e] = diz.get(e, 0) + 1
        # Return the minimum number of complete 'balloon' words that can be formed
        # The word "balloon" requires: 
        #   - 1 'b', 1 'a', 1 'n'
        #   - 2 'l' and 2 'o', so we divide their counts by 2
        return min(diz.get('b', 0), 
                   diz.get('a', 0), 
                   diz.get('l', 0) // 2, 
                   diz.get('o', 0) // 2, 
                   diz.get('n', 0))

            

if __name__ == "__main__":
    
    sos = Solution()
    print(sos.maxNumberOfBalloons(text = "loonbalxballpoon"))