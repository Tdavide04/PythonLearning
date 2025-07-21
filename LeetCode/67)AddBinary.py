'''
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

 

Constraints:

    1 <= a.length, b.length <= 104
    a and b consist only of '0' or '1' characters.
    Each string does not contain leading zeros except for the zero itself.
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        lista = []
        if len(a) > len(b):
            while len(a) > len(b):
                b = "0" + "".join([c for c in b])
            

        if len(a) < len(b):
            while len(a) < len(b):
                a = "0" + "".join([c for c in a])
            
        for e in list(b):
            for i in list(a):
                if b.index(e) == a.index(i):
                    lista.append(e + i)
        return lista
        

if __name__ == "__main__":

    sos = Solution()
    print(sos.addBinary(a = "11", b = "1"))
    

    