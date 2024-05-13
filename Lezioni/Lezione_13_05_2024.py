class Zoo:
    def __init__(self, fences = [], zoo_keepers = []) -> None:
        self.fences = fences
        self.zoo_keepers = zoo_keepers

    def add_fences(self, fence):
        self.fences.append(fence)


    def get_fences(self) -> list:
        return self.fences
    
