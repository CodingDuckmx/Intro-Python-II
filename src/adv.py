from item import Item
from player import Player
from room import Room


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
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
# If the user enters "q", quit the game.

''' Understand - Plan - Execute - Reflect

Questions:

How the end user will interact with the game?
Can the user go back?
Does the game finish when you approach the Chamber?
Are there doors and do the user need items to open doors?
What (other) items the user will found?


Plan:

Starts in the Outside. You can only move north to the Foyer.

We have to ask the player where they want to move.




'''








'''  Game code  '''

user_name = input('Asign a name to the player: ')
playing = True

user = Player(user_name)

print(user)

while playing:

    move = input('Select a movement according to compass: North [N], South [S], East [E], West [W], or Quit [Q]: ').upper()

    if move  == 'Q':
        playing = False

    elif move == 'N':
        user.n_to()
        print(user.croom)
        
    elif move == 'S':
        print(user.croom)

    elif move == 'E':
        print(user.croom)

    elif move == 'W':
        print(user.croom)

    else:
        print(f'Please, select a valid entry and try again. \n Btw, you are in the room: {user.croom}.')

        
        
