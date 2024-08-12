'''
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

1 Whitespace: Ignore any leading whitespace (" ").
2 Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.
3 Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
4 Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.

 

Example 1:

Input: s = "42"

Output: 42

Explanation:

The underlined characters are what is read in and the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
Example 2:

Input: s = " -042"

Output: -42

Explanation:

Step 1: "   -042" (leading whitespace is read and ignored)
            ^
Step 2: "   -042" ('-' is read, so the result should be negative)
             ^
Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
               ^
Example 3:

Input: s = "1337c0d3"

Output: 1337

Explanation:

Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
         ^
Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
             ^
Example 4:

Input: s = "0-1"

Output: 0

Explanation:

Step 1: "0-1" (no characters read because there is no leading whitespace)
         ^
Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
          ^
Example 5:

Input: s = "words and 987"

Output: 0

Explanation:

Reading stops at the first non-digit character 'w'.

 

Constraints:

0 <= s.length <= 200
s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
'''

class Solution:
    def myAtoi(self, s: str) -> int:
        
        # Remove any leading or trailing whitespace from the string
        s = s.strip()
        # If the string is empty after stripping, return 0
        if not s:  
            return 0
        # Convert the string into a list of characters for easier manipulation
        p: list = list(s)
        lista = []
        # Check for a sign at the beginning ('-' or '+')
        if p[0] == "-":
            lista.append("-")  # If it's a negative sign, add it to 'lista'
            p.pop(0)  # Remove the sign from the list 'p'
        elif p[0] == "+":
            p.pop(0)  # Just remove the positive sign, no need to add it to 'lista'
    			   			
        for e in p:
            # If the character is a digit, add it to 'lista'
            if e in "1234567890":
                lista.append(e)
            else:
                # Stop processing if a non-digit character is encountered
                break
            
        # Handle cases where 'lista' might be invalid
        if len(lista) == 0:
            return 0  # If 'lista' is empty, return 0
        elif len(lista) == 1 and lista[0] == "-":
            return 0  # If 'lista' contains only a negative sign, return 0
        
        # Join 'lista' into a string and convert it to an integer
        k = int("".join(lista))

        # Define the 32-bit signed integer range (cause Leetcode can only accept this range)
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        # Clamp the integer 'k' within the 32-bit signed integer range
        if k < INT_MIN:
            return INT_MIN  # If 'k' is less than the minimum, return INT_MIN
        if k > INT_MAX:
            return INT_MAX  # If 'k' is greater than the maximum, return INT_MAX

        return k
        
if __name__ == "__main__":
    
    sos = Solution()
    print(sos.myAtoi("   -042"))

