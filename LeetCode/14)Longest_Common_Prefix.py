'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

 

Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.
'''

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if strs==[]:
            return ""
        strs_lowered = []
        for e in strs:
            strs_lowered.append(e.lower())
        first_str = strs_lowered[0]
        max_prefix = 0
        f = [e for e in strs_lowered]
        f.pop(0)
        for letter in range(len(first_str)):
            for stringa in f:
                if letter >= len(stringa) or stringa[letter] != first_str[letter]:
                    return first_str[:max_prefix]
            
            max_prefix += 1

        return first_str[:max_prefix]


strs = ["Ciao", "ckkkkkkdyi", "Cibo"]
sos = Solution()
print(sos.longestCommonPrefix(strs))