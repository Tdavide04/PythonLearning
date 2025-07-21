'''
Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

    If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
    If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
    Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.

Given an integer, convert it to a Roman numeral.

 

Example 1:

Input: num = 3749

Output: "MMMDCCXLIX"

Explanation:

3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places

Example 2:

Input: num = 58

Output: "LVIII"

Explanation:

50 = L
 8 = VIII

Example 3:

Input: num = 1994

Output: "MCMXCIV"

Explanation:

1000 = M
 900 = CM
  90 = XC
   4 = IV
'''


class Solution:
    def intToRoman(self, num: int) -> str:
        nums = []
        
        while num > 0:
            if num >= 1000:
                num -= 1000
                nums.append("M")
            elif 500 <= num < 1000:
                if 900 <= num <= 999:
                    num -= 900
                    nums.append("CM")
                else:
                    num -= 500
                    nums.append("D")
            elif 100 <= num < 500:
                if 400 <= num <= 499:
                    num -= 400
                    nums.append("CD")
                else:
                    num -= 100
                    nums.append("C")
            elif 50 <= num < 100:
                if 90 <= num <= 99:
                    num -= 90
                    nums.append("XC")
                else:
                    num -= 50
                    nums.append("L")
            elif 10 <= num < 50:
                if 40 <= num <= 49:
                    num -= 40
                    nums.append("XL")
                else:
                    num -= 10
                    nums.append("X")
            elif 5 <= num < 10:
                if num == 9:
                    num -= 9
                    nums.append("IX")
                else:
                    num -= 5
                    nums.append("V")
            elif 1 <= num < 5:
                if num == 4:
                    num -= 4
                    nums.append("IV")
                else:
                    num -= 1
                    nums.append("I")
        nums_join = "".join(nums)
        return nums_join



sus = Solution()
print(sus.intToRoman(3749))