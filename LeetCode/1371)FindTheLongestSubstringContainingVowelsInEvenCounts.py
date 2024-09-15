'''
Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.

 

Example 1:

Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
Example 2:

Input: s = "leetcodeisgreat"
Output: 5
Explanation: The longest substring is "leetc" which contains two e's.
Example 3:

Input: s = "bcbcbc"
Output: 6
Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.
 

Constraints:

1 <= s.length <= 5 x 10^5
s contains only lowercase English letters.
'''


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # Initialize an array to store the first occurrence of each bitmask state
        # We use -2 to signify that a bitmask state has not been encountered yet
        # and -1 to handle the base case where the bitmask is 0 (all vowels are even counts from the start)
        mapy = [-2] * 32
        mapy[0] = -1  # The bitmask 0 is initially seen at index -1

        max_len = 0  # To store the length of the longest valid substring
        mask = 0     # To keep track of the current bitmask state

        # Iterate through each character in the string with its index
        for i, char in enumerate(s):
            # Update the bitmask based on the current vowel
            if char == 'a':
                mask ^= 1   # Toggle the 0th bit for 'a'
            elif char == 'e':
                mask ^= 2   # Toggle the 1st bit for 'e'
            elif char == 'i':
                mask ^= 4   # Toggle the 2nd bit for 'i'
            elif char == 'o':
                mask ^= 8   # Toggle the 3rd bit for 'o'
            elif char == 'u':
                mask ^= 16  # Toggle the 4th bit for 'u'

            # Check if the current bitmask state has been seen before
            prev = mapy[mask]
            if prev == -2:
                # If this bitmask state is encountered for the first time, store its index
                mapy[mask] = i
            else:
                # If the bitmask state has been seen before, calculate the length of the valid substring
                # between the previous occurrence and the current index
                max_len = max(max_len, i - prev)

        return max_len  # Return the length of the longest substring where each vowel appears an even number of times

    
    
if __name__ == "__main__":
    
    sos = Solution()
    print(sos.findTheLongestSubstring("eaiiuaa"))