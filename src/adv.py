from item import Item
from player import Player
from room import Room


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item('stone','A simple stone.'), Item('tree limb','A tree limb ready to be on fire.')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item('gasoline', 'A galon of gasoline.')]),

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

insert_options = ['N','S','E','W','Q']
yes_no = ['Y','N']

user_name = input('Asign a name to the player: ')
playing = True
chamber = False

user = Player(user_name)
user.croom = room['outside']

print(f'Welcome {user.name} to this adventure game, you are in the room {user.croom.name}. \n {user.croom.description}.')
print('To win the game you will have to be able to return to the beginning point safe.')
print('You could die in the darkness, consider that.')
print('Be aware you can only pickup one item per room. Be wise.')
if user.croom.items :
    print(f'In this room you can get this items: {user.croom.items}')
    grab = input('Would you like to grab the stone: Yes [Y] or No [N].')
    
    if grab == 'Y':

        user.croom.items.pop(0)
        user.inventory.append('stone')
        print('Stone has been added to your bag.')

    elif grab == 'N':
 
        grab = input('Would you like to grab the tree limb: Yes [Y] or No [N].')
    
        if grab == 'Y':

            user.croom.items.pop(1)
            user.inventory.append('tree limb')
            print('Tree limb has been added to your bag.')
            user.croom.items.clear()

        elif grab == 'N':

            user.croom.items.clear()
        
        else:
            
            print('Be sure to select Yes [Y] or No [N], please.')

    else:
        
        print('Be sure to select Yes [Y] or No [N], please.')

while playing:


    move = input('Select a movement according to compass: North [N], South [S], East [E], West [W], or Quit [Q]: ').upper()

    if move in insert_options:

        if move  == 'Q':
            playing = False

        else:

            user.move_to(move)
            print(f'You are in in/at {user.croom.name}.')
            if user.croom.items :
                print(f'In this room you can get this items: {user.croom.items}')
                grab = input('Would you like to grab the gasoline: Yes [Y] or No [N].')
                
                if grab == 'Y':

                    user.croom.items.clear()
                    user.inventory.append('gasoline')
                    print('Gasoline has been added to your bag.')

                    light_torch = input('Would you use the gasoline and the limb to turn them into a lighted torch? ')

                    if light_torch == 'Y':

                        user.inventory.clear()
                        user.inventory.append('torch')
                        print('Now with the torch you can see better your way.')

                    elif light_torch == 'N':

                        print('A lighted torch could be good for you.')
                    
                    else:
                        
                        print('Be sure to select Yes [Y] or No [N], please.')


                elif grab == 'N':

                    grab = input('The gasoline would be useful to light a torch.')


                else:
                    
                    print('Be sure to select Yes [Y] or No [N], please.')

            if user.croom.name == 'Treasure Chamber':
                chamber = True

                if 'torch' not in user.inventory:

                    print('You lost.')
                    playing = False

            if user.croom.name == 'Outside Cave Entrance' and 'torch' in user.inventory and chamber == True:

                print("You've won.")
                playing = False

    else:
        print(f'Please, select a valid entry and try again. \n Btw, you are in the room: {user.croom.name}.')

            
            
