'''
Scrivi una funzione che moltiplica tutti i numeri interi di una lista che sono minori di un dato valore intero definito threshold.
For example:

Test	Result
print(moltiplica_numeri([15, 5, 25], 20))
75
'''
def moltiplica_numeri(numbers: list[int], threshold: int) -> int:
    result = 1
    for e in numbers:
        if e < threshold:
            result *= e
    return result