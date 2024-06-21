'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

 

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

 

Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []    
        for char in s:
            if char in '({[':
                stack.append(char)
            else:
                if not stack:
                    return False
                top_element = stack.pop()
                if char == ')' and top_element != '(':
                    return False
                if char == '}' and top_element != '{':
                    return False
                if char == ']' and top_element != '[':
                    return False
        return not stack



s = "(]"
sos = Solution()
print(sos.isValid(s))