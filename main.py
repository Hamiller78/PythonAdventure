# Main game loop for text adventure game

from room import Room

def main():
    # Initialize rooms
    room1 = Room("You are in a dark room. There is a door to the north.")
    room2 = Room("You are in a bright room. There is a door to the south.")
    room3 = Room("You are in a damp cave. There is a door to the east.")
    room4 = Room("You are in a sunny garden. There is a door to the west.")

    # Set up connections
    room1.set_connections({'north': True, 'south': False, 'east': False, 'west': False})
    room2.set_connections({'north': False, 'south': True, 'east': False, 'west': False})
    room3.set_connections({'north': False, 'south': False, 'east': True, 'west': False})
    room4.set_connections({'north': False, 'south': False, 'east': False, 'west': True})

    # Game loop
    while True:
        # print(player.get_current_room().get_description())
        command = input("Enter command (look/move [direction]/quit): ").strip().lower()

        if command == "quit":
            print("Thanks for playing!")
            break
        elif command.startswith("move"):
            direction = command.split()[1]
        #    if player.move(direction):
        #        print(f"You moved {direction}.")
        #    else:
        #        print(f"You can't move {direction} from here.")
        #elif command == "look":
        #    print(player.get_current_room().get_description())
        else:
            print("Invalid command. Try again.")