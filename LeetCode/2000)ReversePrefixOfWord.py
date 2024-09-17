'''
Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

    For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".

Return the resulting string.

 

Example 1:

Input: word = "abcdefd", ch = "d"
Output: "dcbaefd"
Explanation: The first occurrence of "d" is at index 3. 
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".

Example 2:

Input: word = "xyxzxe", ch = "z"
Output: "zxyxxe"
Explanation: The first and only occurrence of "z" is at index 3.
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "zxyxxe".

Example 3:

Input: word = "abcd", ch = "z"
Output: "abcd"
Explanation: "z" does not exist in word.
You should not do any reverse operation, the resulting string is "abcd".

 

Constraints:

    1 <= word.length <= 250
    word consists of lowercase English letters.
    ch is a lowercase English letter.
'''


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        result: str = ""  # Initialize an empty string to store the final result
        for i, char in enumerate(word):  # Iterate through the string, with both index and character
            if char == ch:  # Check if the current character matches 'ch'
                reversed_word = word[:i+1]  # Take the substring from the start to the first occurrence of 'ch'
                reversed_word = reversed_word[::-1]  # Reverse the substring
                result += reversed_word  # Append the reversed substring to the result
                result += word[i+1:]  # Append the rest of the string after 'ch'
                return result  # Return the modified string immediately
        return word  # If 'ch' is not found, return the original word


if __name__ == "__main__":

    sos = Solution()
    print(sos.reversePrefix(word= "siauuumow", ch="u"))