# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self,name, current_room = None, inventory = []):
        self.name = name
        self.croom = current_room
        self.inventory = inventory

    def __str__(self):
        output = f"Player name: {self.name}\n Current Room: {self.croom}."
        
        return output
    
    def move_to(self, direction):
        if direction == "N":
            if self.croom.n_to:
               self.croom = self.croom.n_to
            
            else:
                print("There's no way in that direction.")

        elif direction == 'S':
            if self.croom.s_to:
                self.croom = self.croom.s_to
            
            else:
                print("There's no way in that direction.")
        if direction == "E":
            if self.croom.e_to:
               self.croom = self.croom.e_to
            
            else:
                print("There's no way in that direction.")

        elif direction == 'W':
            if self.croom.w_to:
                self.croom = self.croom.w_to
            
            else:
                print("There's no way in that direction.")
