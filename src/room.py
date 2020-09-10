# Implement a class to hold room information. This should have name and
# description attributes.

from item import Item


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def new_location(self, direction):
        if direction == 'n':
            print("You moved slightly north!")
            return self.n_to
        elif direction == 's':
            print("You moved quite a bit south!")
            return self.s_to
        elif direction == 'e':
            print("You moved rapidly east!")
            return self.e_to
        elif direction == 'w':
            print("You moved quickly west!")
            return self.w_to
        else:
            return None

    def place_item(self, item: Item):
        self.items.append(item)
