class Room:
    def __init__(self, description, connections, items):
        self.__description = description
        self.__connections = connections
        self.__items = items

    def get_description(self):
        return self.__description
    def set_description(self, description):
        self.__description = description

    def get_items(self):
        return self.__items
    def set_items(self, items):
        self.__items = items
    def add_item(self, item):
        self.__items.append(item)
    def remove_item(self, item):
        if item in self.__items:
            self.__items.remove(item)
        else:
            raise ValueError(f"Item '{item}' not found in the room.")
        
    def get_connections(self):
        return self.__connections
    def set_connections(self, connections):
        self.__connections = connections
    
    def connects_to(self, direction):
        if direction in self.__connections:
            return self.__connections[direction]
        return None
    def add_connection(self, direction, room):
        self.__connections[direction] = room
    def remove_connection(self, direction):
        if direction in self.__connections:
            del self.__connections[direction]
        else:
            raise KeyError(f"Connection '{direction}' not found.")