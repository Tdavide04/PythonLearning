'''
Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format.

The final result should be an irreducible fraction. If your final result is an integer, change it to the format of a fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.

 

Example 1:

Input: expression = "-1/2+1/2"
Output: "0/1"
Example 2:

Input: expression = "-1/2+1/2+1/3"
Output: "1/3"
Example 3:

Input: expression = "1/3-1/2"
Output: "-1/6"
 

Constraints:

The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
Each fraction (input and output) has the format ±numerator/denominator. If the first input fraction or the output is positive, then '+' will be omitted.
The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will always be in the range [1, 10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
The number of given fractions will be in the range [1, 10].
The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.
'''

class Solution:
    # def gcd(self, a:int, b: int) -> int:
    #     while b:
    #         a = b
    #         b = a % b
    #     return a

    # def lcm(self, a:int, b: int) -> int:
    #     return abs(a*b) // self.gcd(a,b)
        
    def fractionAddition(self, expression: str) -> str:
        if expression[0] != '-':
            expression = '+' + expression
        terms: list = []
        
        return terms

    
if __name__ == "__main__":
    
    sos = Solution()
    print(sos.fractionAddition(expression= "-1/2+1/2")) # Output: "0/1"
    print(sos.fractionAddition(expression= "-1/3+1/4-1/5+1/6-1/7+1/8-1/9+1/10-1/11+1/12")) # Output: "-4247/27720"
    print(sos.fractionAddition(expression= "1/10-1/10")) # Output: "0/1"
    print(sos.fractionAddition(expression= "1/3-1/2")) # Output: "-1/6"
    print(sos.fractionAddition(expression= "1/6-1/6+2/3-2/3")) # Output: "0/1"
    print(sos.fractionAddition(expression= "1/4+3/4")) # Output: "1/1"
    print(sos.fractionAddition(expression= "9/4-5/3+7/2-9/5+10/6-1/7+1/8-2/9+2/10")) # Output: "9853/2520"
    print(sos.fractionAddition(expression= "-1/1-1/1-1/1-1/1-1/1-1/1-1/1-1/1-1/1-1/1")) # Output: "-10/1"
    print(sos.fractionAddition(expression= "-1/3-1/4-1/5-1/6-1/7-1/8-1/9-1/10-1/10-6/10")) # Output: "-1073/504"