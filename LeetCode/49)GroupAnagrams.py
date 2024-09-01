'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Initialize a defaultdict where each key maps to a list.
        # This will store lists of anagrams grouped by their sorted tuple form.
        hashmap = defaultdict(list)
        result: list = [] # This will store the final grouped anagrams before returning.
        for string in strs: # Iterate over each string in the input list.
            # Sort the characters in the string and convert it to a tuple.
            # The tuple will serve as a key to group anagrams together.
            sorted_string = tuple(sorted(string))
            # Append the original string to the list in the hashmap under the sorted tuple key.
            hashmap[sorted_string].append(string)
        # Iterate over the lists of anagrams in the hashmap.
        for value in hashmap.values():
            result.append(value) # Append each list of anagrams to the result list.
        return result
