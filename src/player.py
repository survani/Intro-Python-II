# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = []


    def move_player(self, direction):
        new_room = self.room.new_location(direction)
        if new_room is not None:
            self.room = new_room

    def get_item(self, item, room):
        self.items.append(item)
        print(f"You know have obtain x1 ({item}) from {room}")
