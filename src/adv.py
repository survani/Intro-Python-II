from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game

# Welcome Message
message = "Welcome to the Adventure Game!"
print(message)

# Choose Player name
player_name = input("Please enter your player's name -> ")

# New Player Object
main_player = Player(player_name, room['outside'])

# Game started message
print(f"Nice to see you here {main_player.name}! If you ever want to quit the game make sure you type 'q'")

# Directions a player can make
directions = ["n", "s", "e", "w"]

# Game logic (loop starts here)

while True:
    print(f"Located: {main_player.room.name}")
    print(f"Description: {main_player.room.description}")

    player_input = input("Choose what direction you want to travel ['n', 's', 'e', 'w'] -> ")

    if player_input == "q":
        print("Thanks for playing our game!")
        break
    elif player_input in directions:
        main_player.move_player(player_input)
    elif player_input != directions:
        print("Please use the correct text inputs!")
