'''
A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

 

Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"

Output: ["sweet","sour"]

Explanation:

The word "sweet" appears only in s1, while the word "sour" appears only in s2.

Example 2:

Input: s1 = "apple apple", s2 = "banana"

Output: ["banana"]

 

Constraints:

    1 <= s1.length, s2.length <= 200
    s1 and s2 consist of lowercase English letters and spaces.
    s1 and s2 do not have leading or trailing spaces.
    All the words in s1 and s2 are separated by a single space.
'''


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        # Split both input sentences by spaces and concatenate the resulting lists into s3
        s3: str = s1.split(" ") + s2.split(" ")
        # Initialize an empty dictionary to keep track of word counts
        diz: dict = {}
        # Initialize an empty list to store the result
        result: list = []
        # Iterate over each word in the concatenated list of words
        for char in s3:
            # If the word is not in the dictionary, add it with a count of 1
            if char not in diz:
                diz[char] = 1
            # If the word is already in the dictionary, increment its count by 1
            else:
                diz[char] += 1
        # Iterate through the dictionary to check word counts
        for key, val in diz.items():
            # If a word appears exactly once, add it to the result list
            if val == 1:
                result.append(key)
        return result

    

if __name__ == "__main__":

    sos = Solution()
    print(sos.uncommonFromSentences("ciao ciao", "ciao"))