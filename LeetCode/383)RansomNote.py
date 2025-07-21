'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_list = [e for e in magazine]
        for e in ransomNote:
            if e not in magazine_list:
                return False
            magazine_list.remove(e)
        return True
            
    
if __name__ == "__main__":
    
    sos = Solution()
    print(sos.canConstruct(ransomNote="aerta", magazine="bdortsena"))
    