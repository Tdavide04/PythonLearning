from room import Room
from building import Building


r = Room(name = "213", floor = 2, num_seets=30)
print(r)

b = Building(name = "SMI", address = "Via della Sierra Nevada", floors = 5)
print(b)
print(len(b.get_rooms()))