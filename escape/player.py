"""Module: Define Player and Rooms"""

import items as it
from story import menu_text

ROOMS = {
    1: {"name": "White Room",
        "north": it.BLUE_DOOR,
        "item": it.PACK, "orb": it.BLUE_ORB},
    2: {"name": "Blue Room",
        "south": it.WHITE_DOOR, "east": it.GREEN_DOOR,
        "west": it.PURPLE_DOOR,
        "orb": it.GREEN_ORB},
    3: {"name": "Green Room",
        "west": it.BLUE_DOOR, "north": it.YELLOW_DOOR,
        "orb": it.PURPLE_ORB},
    4: {"name": "Purple Room",
        "east": it.BLUE_DOOR, "north": it.RED_DOOR,
        "orb": it.RED_ORB},
    5: {"name": "Red Room",
        "south": it.PURPLE_DOOR, "east": it.ORANGE_DOOR,
        "orb": it.YELLOW_ORB},
    6: {"name": "Yellow Room",
        "south": it.GREEN_DOOR, "west": it.ORANGE_DOOR,
        "orb": it.ORANGE_ORB},
    7: {"name": "Orange Room",
        "east": it.YELLOW_DOOR, "west": it.RED_DOOR,
        "north": it.BLACK_DOOR,
        "orb": it.WHITE_ORB},
    8: {"name": "Black Room",
        "south": it.ORANGE_DOOR,
        "item": it.TWIZZLERS}
}


class Player():
    """Establish Player gameplay"""
    def __init__(self, room=1, inventory=set()):
        self.room = room
        self.inventory = inventory

    def menu(self):
        """List main menu"""
        line_1 = "_" * 47
        space = " " * 17

        print("\n" + line_1)
        print(space + "Valid Commands")
        print(menu_text)
        print(line_1 + "\n")
        # command: > 'ending'  (prompts end-game w/text)
        # command: > 'port [room_tag] ('one' == ROOMS[1], 'seven' == ROOMS[7])

    def stats(self):
        """Broadcast current status"""
        line_2 = "-" * 30
        location = ROOMS[self.room]

        print("\n" + line_2)
        print("You are in : " + location["name"])
        if it.PACK in self.inventory:
            print(it.PACK.contents())
        if "item" in location:
            print("You catch sight of a {}".format(location["item"]))
        if "orb" in location:
            print("You catch sight of a {}".format(location["orb"]))
        print(line_2 + "\n")

    def match(self, door):
        """Check PACK for Orb match"""
        for x in it.PACK.pocket:
            if x.icolor() == door.icolor():
                return True

    def check(self, obj):
        """Check Item for details"""
        location = ROOMS[self.room]

        print("You take a closer look at the {}...".format(obj))
        print(obj.info())
        print("You discover a {}".format(obj.hidden())
              + " hidden inside the {}!".format(obj))
        if obj == it.SHELF:
            location["Orb"] = it.SHELF.hidden()
        else:
            location["Item"] = it.SHRINE.hidden()

    def move(self, direction):
        """Move in desired direction"""
        door = ROOMS[self.room][str(direction)]

        if door.lock_status(False):
            self.room = door.room_tag()
        elif door.lock_status(True):
            print("\nYou encounter " + it.door_desc(door.icolor()))
            if it.PACK in self.inventory and self.match(door):
                door.unlock()
                self.room = door.room_tag()
            else:
                print("The door doesn't budge!")

    def action(self):
        """Establish Player action"""
        choice = input("> ").lower().split()
        choices = ("options", "check", "go", "get", "gg", "port")
        location = ROOMS[self.room]

        if choice[0] == "options":
            self.menu()
        elif choice[0] == "check":
            if choice[1] == "item":
                self.check(location["item"])
            elif choice[1] == "orb":
                self.check(location["orb"])
            else:
                print("\nIt must have been your imagination")
        elif choice[0] == "go":
            if choice[1] == "north" and choice[1] in location:
                self.move("north")
            elif choice[1] == "east" and choice[1] in location:
                self.move("east")
            elif choice[1] == "south" and choice[1] in location:
                self.move("south")
            elif choice[1] == "west" and choice[1] in location:
                self.move("west")
            else:
                print("\nYou cannot go that way!\n")
        elif choice[0] == "get":
            if choice[1] == "item" and "item" in location:
                if location["item"] == it.PACK:
                    self.inventory.add(it.PACK)
                else:
                    it.PACK.add_pack(location["item"])
                print("\nPicked up {}!".format(location["item"]))
                print(location["item"].info())
                del location["item"]
            elif choice[1] == "orb" and "orb" in location:
                if it.PACK in self.inventory:
                    it.PACK.add_pack(location["orb"])
                    print("\nPicked up {}!".format(location["orb"]))
                    print(location["orb"].info())
                    del location["orb"]
                else:
                    print("\nYou should have worn the pants with pockets!")
            else:
                print("\nIt must have been a mirage...")
        while choice[0] == "gg":
            exit_choice = input(
                "\nAre you sure you wish to quit? Choose [Y] or [N]: ").lower()
            if exit_choice == "y":
                quit()
            elif exit_choice == "n":
                break
            else:
                print("\nThat's not a valid choice.")
                continue
        if choice[0] == "port":  # Teleport for easy ROOM testing
            if choice[1] == "one":
                self.room = 1
            elif choice[1] == "seven":
                self.room = 7
            else:
                return "You can't envision this location in your mind's eye"
        if choice[0] not in choices:
            print("\nThat's not a valid command!")
