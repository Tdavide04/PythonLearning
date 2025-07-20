def sum_above_threshold(numbers: list[int], target) -> int:
    
    lista = []
    for e in numbers:
        if e > target:
            lista.append(e)
    return sum(lista)