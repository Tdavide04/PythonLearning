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

