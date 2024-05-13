class Room:

    def __init__(self, name: str, floor: int, num_seets: int) -> None:
        self.set_name = name
        self.set_floor(floor)
        self.set_num_seets(num_seets)

    def set_name(self, name: str):
        self.name = name 

    def set_floor(self, floor: int):
        self.floor = floor

    def set_num_seets(self, num_seets: int):
        self.num_seets = num_seets

    def get_name(self) -> str:
        return self.name
    
    def get_floor(self) -> int:
        return self.floor
    
    def get_num_seets(self) -> int:
        return self.num_seets
    
    def __str__(self):
        pass