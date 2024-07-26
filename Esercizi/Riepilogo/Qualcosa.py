def transform(x: int) -> int:
    
    if x % 2 == 0:
        x /= 2
    else:
        x = (x * 3) - 1
    return x