'''
You are given a string s consisting of lowercase English letters, and an integer k.

First, convert s into an integer by replacing each letter with its position in the alphabet (i.e., replace 'a' with 1, 'b' with 2, ..., 'z' with 26). Then, transform the integer by replacing it with the sum of its digits. Repeat the transform operation k times in total.

For example, if s = "zbax" and k = 2, then the resulting integer would be 8 by the following operations:

    Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
    Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
    Transform #2: 17 ➝ 1 + 7 ➝ 8

Return the resulting integer after performing the operations described above.

 

Example 1:

Input: s = "iiii", k = 1
Output: 36
Explanation: The operations are as follows:
- Convert: "iiii" ➝ "(9)(9)(9)(9)" ➝ "9999" ➝ 9999
- Transform #1: 9999 ➝ 9 + 9 + 9 + 9 ➝ 36
Thus the resulting integer is 36.

Example 2:

Input: s = "leetcode", k = 2
Output: 6
Explanation: The operations are as follows:
- Convert: "leetcode" ➝ "(12)(5)(5)(20)(3)(15)(4)(5)" ➝ "12552031545" ➝ 12552031545
- Transform #1: 12552031545 ➝ 1 + 2 + 5 + 5 + 2 + 0 + 3 + 1 + 5 + 4 + 5 ➝ 33
- Transform #2: 33 ➝ 3 + 3 ➝ 6
Thus the resulting integer is 6.

Example 3:

Input: s = "zbax", k = 2
Output: 8

 

Constraints:

    1 <= s.length <= 100
    1 <= k <= 10
    s consists of lowercase English letters.
'''

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Convert each character in the string s to its corresponding position in the alphabet
        # 'a' -> 1, 'b' -> 2, ..., 'z' -> 26
        # This is done using the ord() function and list comprehension
        number = [str(ord(char) - ord("a") + 1) for char in s.lower() if char.isalpha()]
        # Combine all the number strings into one large number string
        large_num = "".join(number)
        # Perform the transformation process k times
        while k != 0:
            # Initialize a sum variable to store the sum of the digits
            summ = 0
            # Iterate over each digit in the large number string and sum them up
            for num in large_num:
                summ += int(num)
            # Update large_num with the new sum as a string
            large_num = str(summ)
            # Decrement the transformation count
            k -= 1
        return int(large_num)

if __name__ == "__main__":

    sos = Solution()
    print(sos.getLucky(s = "iiii", k = 1))