'''
Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5
 

Constraints:

-1000 <= a, b <= 1000
'''

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Create a mask to simulate 32-bit integer behavior
        # pow(2, 32) gives us 2^32, which is 4294967296, and subtracting 1 gives 0xFFFFFFFF (32-bit mask).
        mask = pow(2, 32) - 1
        
        # Continue the loop until there is no carry left (b becomes 0)
        # Using `b & mask` ensures that we only consider the lower 32 bits of b,
        # simulating 32-bit integer arithmetic as Python supports arbitrarily large integers.
        while b & mask:
            # XOR operation gives the sum of a and b without considering carries
            # This stores the intermediate sum without carry in `a`
            a, b = a ^ b, (a & b) << 1  # AND operation finds the carry positions, and shifting left moves carry to the next significant bit
            
        # The loop terminates when b becomes 0, meaning there are no more carries.
        
        # Now, we return the final result. If `b` is positive (meaning it's a small positive number),
        # we ensure the result stays within 32 bits by applying the mask to `a`.
        # If `b` is not positive (i.e., we have handled all carries), we return `a`.
        # If `a` is negative, it already represents the final result.
        return a & mask if b > 0 else a

    
    
if __name__ == "__main__":
    
    sos = Solution()