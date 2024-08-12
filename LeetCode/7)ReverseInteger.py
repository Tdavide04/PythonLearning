'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
'''

class Solution:
    def reverse(self, x: int) -> int:
        
        
        x = list(str(x)) # Convert the integer x to a list of characters (strings).
        lista: list = []
        if x[0] == "-": # Check if the first character is a negative sign.
            lista.append("-") # If it is, add the negative sign to the result list (lista).
            x.pop(0) # Remove the negative sign from the original list x.
        for e in x[::-1]: # Loop through the remaining characters in x in reverse order.
            lista.append(e) # Append each character to the result list (lista).
        reversed_num = int(("".join(lista))) # Join the list into a single string and convert it back to an integer.
        
        # Define the 32-bit signed integer range limits.
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        # Check if the reversed number is less than the minimum allowed value.
        if reversed_num < INT_MIN:
            return 0
        # Check if the reversed number is greater than the maximum allowed value.
        if reversed_num > INT_MAX:
            return 0  
        # If the reversed number is within the 32-bit integer range, return it.
        return reversed_num


if __name__ == "__main__":
    
    sos = Solution()
    print(sos.reverse(-123))