"""Module: Define Items"""


class Item(object):
    """Define basic Item"""
    def __init__(self, name, description, tag):
        self.name = name
        self.description = description
        self.tag = tag

    def __repr__(self):
        """Return alternate Item name"""
        return self.name

    def __str__(self):
        """Return true Item name"""
        return "[{}]".format(self.name)

    def info(self):
        """Return detailed description"""
        return ("\n[{}]\n"
                + "=" * (len(self.name) + 2)
                + "\n{}").format(self.name, self.description)

    def room_tag(self):
        """Return original location of Item"""
        return self.tag


class Pack(Item):
    """Define Pack"""
    def __init__(self):
        super().__init__(name="Leather Pack",
                         description="Even the pockets have pockets!",
                         tag=1)
        self.pocket = []

    def add_pack(self, obj):
        self.pocket.append(obj)

    def contents(self):
        """Return current iventory"""
        if self.pocket == []:
            return "Inventory: Empty"
        elif len(self.pocket) > 4:
            return ("Inventory: {}\n".format(self.pocket[:4])
                    + (" " * 11) + "{}.".format(self.pocket[4:]))
        else:
            return "Inventory: {}".format(self.pocket)


class Checkable(Item):
    """Define Checkable Item"""
    def __init__(self, name, description, tag, obj):
        super().__init__(name, description, tag)
        self.obj = obj
        self.hidden = [obj]

    def hidden(self):
        """Return that which lies beneath"""
        return self.hidden[0]


class Orb(Item):
    """Define Orbs"""
    def __init__(self, name, description, tag, color):
        super().__init__(name, description, tag)
        self.color = color

    def icolor(self):
        """Return color"""
        return self.color


class Door(Orb):
    """Define Doors"""
    def __init__(self, name, description, tag, color, lock=True):
        super().__init__(name, description, tag, color)
        self.lock = lock

    def rezonate(self):
        """Rezonate with Orb"""
        print("""You raise the {} orb in front of you.
        The door vibrates in sync with the orb and begins to open!
        """.format(self.color))

    def lock_status(self, condition):
        """Return status of lock"""
        if self.lock == condition:
            return True
        else:
            return False

    def unlock(self):
        """Unlock Door"""
        self.lock = False
        self.rezonate()


def door_desc(color):
    """Return Door encounter description text"""
    return "an impossing stone door with a feint {} glow.".format(color)


# Orbs
BLUE_ORB = Orb("Blue Orb", "A glowing blue orb", 2, "blue")
GREEN_ORB = Orb("Green Orb", "A glowing green orb", 2, "green")
PURPLE_ORB = Orb("Purple Orb", "A glowing purple orb", 3, "purple")
RED_ORB = Orb("Red Orb", "A glowing red orb", 4, "red")
YELLOW_ORB = Orb("Yellow Orb", "A glowing yellow orb", 5, "yellow")
ORANGE_ORB = Orb("Orange Orb", "A glowing orange orb", 6, "orange")
WHITE_ORB = Orb("White Orb", "A glowing white orb", 7, "white")
BLACK_ORB = Orb("Black Orb", "A glowing black orb", 1, "black")
# Doors
BLUE_DOOR = Door("Blue Door", door_desc("blue"), 2, "blue")
GREEN_DOOR = Door("Green Door", door_desc("green"), 3, "green")
PURPLE_DOOR = Door("Purple Door", door_desc("purple"), 4, "purple")
RED_DOOR = Door("Red Door", door_desc("red"), 5, "red")
YELLOW_DOOR = Door("Yellow Door", door_desc("yellow"), 6, "yellow")
ORANGE_DOOR = Door("Orange Door", door_desc("orange"), 7, "orange")
WHITE_DOOR = Door("White Door", door_desc("white"), 1, "white")
BLACK_DOOR = Door("Black Door", door_desc("black"), 8, "black")
# Items
PACK = Pack()
TWIZZLERS = Item("Pack of Twizzlers", "The tastiest of tasty snacks!", 8)
SHRINE = Checkable("Old Shrine",
                   "An ornate box sits atop an onyx pedestal",
                   8,
                   TWIZZLERS)
SHELF = Checkable("Bookshelf",
                  ("A bookshelf housing old leather tomes."
                   "\nOne of the books seems out of place..."),
                  2,
                  GREEN_ORB)
