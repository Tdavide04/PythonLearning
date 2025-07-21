'''
Scrivere un frammento di codice che modifichi il valore intero memorizzato nella variabile n nel seguente modo:
se n è pari, deve essere incrementato di 10;
se n è dispari, deve essere decrementato di 5.
For example:

Test	Result
n1 = 8
print(modifica_valore(n1))
18
n4 = -4
print(modifica_valore(n4))
6
'''

def modifica_valore(n: int) -> int:
    if n % 2 == 0:
        n += 10
    else:
        n -= 5
    return n