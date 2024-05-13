from room import Room

class Building:

    def __init__(self, name: str, address: str, floors: int):
        self.name = name
        self.address = address
        self.floors = floors
        self.rooms = []

    def add_room(room: Room) -> bool:
        if room not in self.get_rooms() and room.floor <= self.get_floors():
            self.rooms.append(room)
            return True
        return False

    def get_room(self) -> str:
        return self.name
    
    def get_address(self) -> str:
        return self.address
    
    def get_floors(self):
        return self.floors
    
    def get_rooms(self):
        return self.rooms
    
    def __str__(self) -> str:
        s: str = f"Building(name = {self.get_name()}, address = {self.get_address()}, floors = {self.get_floors})"
        