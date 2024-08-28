'''
Scrivi una funzione che verifica se una combinazione di condizioni (X, Y, e Z) è soddisfatta per procedere con un'azione. L'azione può procedere solo se la condizione X è vera e almeno una tra Y e Z è vera. La funzione deve ritornare "Azione permessa" oppure "Azione negata" a seconda delle condizioni che sono soddisfatte.
For example:

Test	Result
print(verifica_condizioni(True, False, True))
Azione permessa
print(verifica_condizioni(True, False, False))
Azione negata
'''

def verifica_condizioni(X: bool, Y: bool, Z: bool) -> str:
    if X == True and Y == True or Z == True:
        return "Azione permessa"
    return "Azione negata"