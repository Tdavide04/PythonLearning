'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

 

Constraints:

    1 <= s.length <= 15
    s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    It is guaranteed that s is a valid roman numeral in the range [1, 3999].
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        i = 0

        while i < len(s):
            if s[i:i+2] == "IV":
                num += 4
                i += 2
            elif s[i:i+2] == "IX":
                num += 9
                i += 2
            elif s[i:i+2] == "XL":
                num += 40
                i += 2
            elif s[i:i+2] == "XC":
                num += 90
                i += 2
            elif s[i:i+2] == "CD":
                num += 400
                i += 2
            elif s[i:i+2] == "CM":
                num += 900
                i += 2
            elif s[i] == "I":
                num += 1
                i += 1
            elif s[i] == "V":
                num += 5
                i += 1
            elif s[i] == "X":
                num += 10
                i += 1
            elif s[i] == "L":
                num += 50
                i += 1
            elif s[i] == "C":
                num += 100
                i += 1
            elif s[i] == "D":
                num += 500
                i += 1
            elif s[i] == "M":
                num += 1000
                i += 1

        return num
    

sos = Solution()
print(sos.romanToInt("MCMXCIV"))