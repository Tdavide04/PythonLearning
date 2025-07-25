'''
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer num, return its complement.

 

Example 1:

Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:

Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
 

Constraints:

1 <= num < 231
 

Note: This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/
'''

class Solution:
    def findComplement(self, num: int) -> int:
        # Convert the number to its binary representation, remove the '0b' prefix with [2:],
        # and convert it into a list of characters.
        bin_num: list = list(bin(num)[2:])
        for e in range(len(bin_num)):
            if bin_num[e] == '1':
                bin_num[e] = '0'
            else:
                bin_num[e] = '1'
        # Join the list back into a string, convert it to an integer with base 2,
        # which gives us the complement in decimal form. 
        complementary_num = int("".join(bin_num), 2)
        return complementary_num
    
if __name__ == "__main__":
    
    sos = Solution()
    print(sos.findComplement(num = 5))