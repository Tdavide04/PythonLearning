'''
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer n, return its complement.

 

Example 1:

Input: n = 5
Output: 2
Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.
Example 2:

Input: n = 7
Output: 0
Explanation: 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.
Example 3:

Input: n = 10
Output: 5
Explanation: 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.
 

Constraints:

0 <= n < 109
 

Note: This question is the same as 476: https://leetcode.com/problems/number-complement/
'''

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # Convert the number to its binary representation, remove the '0b' prefix with [2:],
        # and convert it into a list of characters.
        bin_num: list = list(bin(n)[2:])
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
    print(sos.bitwiseComplement(n=7))