'''
Scrivere la funzione chiamata seconds_since_noon che riceva il tempo espresso come tre argomenti interi (ore, minuti e secondi) e restituisca il numero dei secondi da quando l'orologio "ha battuto le 12" l'ultima volta (le ore 12, dunque, vengono considerate come orario di partenza, dunque, come uno zero).

Ad esempio, alle ore 3:15:50 sono passate 3 ore, 15 minuti e 50 secondi, ovvero sono passati 11750 secondi da quando l'orologio ha "battuto le 12" per l'ultima volta.

Definire, poi, la funzione chiamata time_difference che prende come argomento due orari, entrambi espressi mediante ore, minuti e secondi. La funzione time_difference deve usare la funzione seconds_since_noon per calcolare la quantità di tempo in secondi tra due orari, entrambi contenuti entro un ciclo dell'orologio di 12 ore.

Ad esempio, tra le ore 1:00 e 3:15:30 sono passati 8130 secondi.
For example:

Test	Result
print(time_difference(1, 0, 0, 3, 15, 30))
8130
print(time_difference(0, 0, 0, 12, 0, 0))
43200
'''

def seconds_since_noon(ore, minuti, secondi):
    if ore < 24:
        ore_secondi = ore * 3600
    if minuti < 60:
        minuti_secondi = minuti * 60
    secondi_totali = ore_secondi + minuti_secondi + secondi
    return secondi_totali

def time_difference(ore1, minuti1, secondi1, ore2, minuti2, secondi2):
    first = seconds_since_noon(ore1, minuti1, secondi1)
    second = seconds_since_noon(ore2, minuti2, secondi2)
    result = abs(second - first)
    return result