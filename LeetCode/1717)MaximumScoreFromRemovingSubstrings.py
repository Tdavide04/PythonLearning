'''
You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.

 

Example 1:

Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.
Example 2:

Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20
 

Constraints:

1 <= s.length <= 105
1 <= x, y <= 104
s consists of lowercase English letters.
'''
class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        
        right = 0
        sum = 0
        s1 = list(s)
        while(right < len(s1) - 1):
            
            if (s1[right] == "a" and s1[right + 1] == "b"):
                sum += x
                s1.pop(right)
                s1.pop(right)
                right = -1
            elif (s1[right] == "b" and s1[right + 1] == "a"):
                sum += y
                s1.pop(right)
                s1.pop(right)
                right = -1
            right += 1
        return sum
            
if __name__ == "__main__":
    sos = Solution()
    print(sos.maximumGain(s = "cdbcbbaaabab", x = 4, y = 5)) #19