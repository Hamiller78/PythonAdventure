# Add class for player with position and inventory

class Player:
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.inventory = []

    def set_current_room(self, room):
        self.current_room = room
    def get_current_room(self):
        return self.current_room
    
    def get_inventory(self):
        return self.inventory
    def add_to_inventory(self, item):
        self.inventory.append(item)
    def remove_from_inventory(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            raise ValueError(f"Item '{item}' not found in inventory.")