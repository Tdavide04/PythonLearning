'''
You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.

 

Example 1:

Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.

Example 2:

Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.

Example 3:

Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.

 

Constraints:

    1 <= words.length <= 104
    1 <= allowed.length <= 26
    1 <= words[i].length <= 10
    The characters in allowed are distinct.
    words[i] and allowed contain only lowercase English letters.
'''

class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        result: int = 0  # This will store the count of consistent strings
        # Iterate through each word in the list of words
        for word in words:
            # Check each character in the current word
            for char in word:
                # If the character is not in the allowed string, it's not consistent
                if char not in allowed:
                    result -= 1  # Decrease result if the word is inconsistent
                    break  # Break out of the inner loop since this word is invalid
            
            result += 1  # Increment result after finishing the word check
        return result  # Return the total count of consistent strings
    

class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        result: int = 0
        i: int = 0
        for word in words:
            while i < len(allowed):
                if allowed[i] in word:
                    word = word.replace(allowed[i], "")
                i += 1
            i = 0
            if word == "":
                result += 1
        return result



if __name__ == "__main__":

    sos = Solution()
    print(sos.countConsistentStrings(allowed = "ab", words = ["aaab","baa","badab"]))