'''
Given a positive integer num represented as a string, return the integer num without trailing zeros as a string.

 

Example 1:

Input: num = "51230100"
Output: "512301"
Explanation: Integer "51230100" has 2 trailing zeros, we remove them and return integer "512301".

Example 2:

Input: num = "123"
Output: "123"
Explanation: Integer "123" has no trailing zeros, we return integer "123".

 

Constraints:

    1 <= num.length <= 1000
    num consists of only digits.
    num doesn't have any leading zeros.
'''

class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        num: list = list(num)
        for number in num[::-1]:
            if number == "0":
                num.pop()
            else:
                return "".join(num)
            
if __name__ == "__main__":

    sos = Solution()
    print(sos.removeTrailingZeros())