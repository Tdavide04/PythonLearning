import unittest

class Calculations:

    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    def get_sum(self):
        return self.a + self.b

    def get_difference(self):
        return self.a - self.b
    
    def get_product(self):
        return self.a * self.b
    
    def get_quotient(self):
        if self.b == 0:
            raise ValueError("Cannot divide by zero")
        return self.a / self.b
    
calc = Calculations("10", 5)
print(calc.get_product())