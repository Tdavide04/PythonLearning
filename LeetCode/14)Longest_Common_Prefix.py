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
        strs_lower = []
        lista=[]
        i=0

        for e in strs:
            strs_lower.append(e.lower())
        for e in strs:  
            while i<=len(max(strs)):
                if 


        for e in strs_lower:
            pass

strs = ["Ciao", "cane", "Cibo"]
sos = Solution()
print(sos.longestCommonPrefix(strs))