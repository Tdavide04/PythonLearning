'''
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

Example 2:

Input: num = 0
Output: 0

 

Constraints:

    0 <= num <= 231 - 1

 

Follow up: Could you do it without any loop/recursion in O(1) runtime?
'''

class Solution:
    def addDigits(self, num: int) -> int:
        # Convert the input number to a string to iterate over each digit
        num = str(num)
        # Continue the process until the number has only one digit
        while len(num) != 1:
            # Initialize a variable to store the sum of the digits
            summ = 0
            # Loop through each character (digit) in the string representation of the number
            for e in num:
                # Add the integer value of the current digit to the sum
                summ += int(e)
            # Update num to be the string representation of the new sum
            num = str(summ)
        return int(num)


if __name__ == "__main__":

    sos = Solution()
    print(sos.addDigits(num = 38))