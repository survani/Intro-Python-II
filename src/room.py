# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def new_location(self, direction):
        if direction == 'n':
            print("You just walked north!")
            return self.n_to
        elif direction == 's':
            print("You just walked south!")
            return self.s_to
        elif direction == 'e':
            print("You just walked east!")
            return self.e_to
        elif direction == 'w':
            print("You just walked west!")
            return self.w_to
        else:
            return None

    def __str__(self):
        return f"{self.name} {self.description}"
