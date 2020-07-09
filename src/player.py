# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self,name, current_room = 'outside'):
        self.name = name
        self.croom = current_room

    def __str__(self):
        output = f"Player name: {self.name}\n Current Room: {self.croom}"
        
        return output
    
    def n_to(self):


        if self.croom == 'outside':
            self.croom = 'foyer'
        elif self.croom == 'foyer':
            self.croom == 'overlook'
        elif self.croom == 'narrow':
            self.croom == 'treasure'
        else:
            print("There's no way North.")

