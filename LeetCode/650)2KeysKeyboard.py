'''
There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad for each step:

Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.

 

Example 1:

Input: n = 3
Output: 3
Explanation: Initially, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.
Example 2:

Input: n = 1
Output: 0
 

Constraints:

1 <= n <= 1000
'''

class Solution:
    def minSteps(self, n: int) -> int:
        # If n is 1, no steps are needed since we already have 'A'
        if n == 1:
            return 0
        
        steps = 0  # Initialize the count of steps
        factor = 2  # Start checking for factors from 2 (the smallest prime number)
        
        # Continue until n is reduced to 1
        while n > 1:
            # While n is divisible by the current factor
            while n % factor == 0:
                steps += factor  # Add the factor to the step count
                n //= factor  # Divide n by the factor to reduce it
            
            factor += 1  # Move to the next potential factor
        
        # Return the total number of steps
        return steps

    
    
if __name__ == "__main__":
    
    sos = Solution()
    print(sos.minSteps(n = 111))