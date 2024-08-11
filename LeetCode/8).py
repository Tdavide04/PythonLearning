class Solution:
    def myAtoi(self, s: str) -> int:
        p: list = list(s)
        lista = []
        if p[0] == "-":
            lista.append("-")
            p.remove(p[0])
    			   			
        for e in p:
            if e in "1234567890":
                lista.append(e)
            else:
                break
        if lista[0] == "-" and lista[1] == "0":
            lista.remove(lista[1])		
        return int("".join(lista))
 
sos = Solution()
print(sos.myAtoi("1337c0d3"))