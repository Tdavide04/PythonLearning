def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    
    if conditionA == True:
        return "Operazione permessa"
    if conditionB == True and conditionC == True:
        return "Operazione permessa"
    else:
        return "Operazione negata"