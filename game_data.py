"""CSC111 Project 1: Text Adventure Game Classes

Instructions (READ THIS FIRST!)
===============================

This Python module contains the main classes for Project 1, to be imported and used by
 the `adventure` module.
 Please consult the project handout for instructions and details.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 CSC111 Teaching Team
"""
from typing import Optional, TextIO
import climage


class Item:
    """An item in our text adventure game world.

    Instance Attributes:
        - name: name of the item
        - id: special integer id of the item
        - init_location: where the item initially is
        - short_description: brief description of the item
        - long_description: specific description of the item
        - score: score earn by taking this item
        - can_earn: socre can be only earned when item is taken for the first time

    """
    name: str
    item_id: int
    curr_location: list[int]
    short_description: str
    long_description: str
    score: float
    can_add: bool
    can_earn: bool

    def __init__(self, name: str, item_id: int, location_x: int, location_y: int,
                 short_description: str, long_description: str, score: float) -> None:
        """Initialize a new item.
        """

        # NOTES:
        # This is just a suggested starter class for Item.
        # You may change these parameters and the data available for each Item object as you see fit.
        # (The current parameters correspond to the example in the handout).
        # Consider every method in this Item class as a "suggested method".
        #
        # The only thing you must NOT change is the name of this class: Item.
        # All item objects in your game MUST be represented as an instance of this class.

        self.name = name
        self.item_id = int(item_id)
        self.curr_location = [int(location_x), int(location_y)]
        self.short_description = short_description
        self.long_description = long_description
        self.score = float(score)
        self.can_add = True
        self.can_earn = True


class Location:
    """A location in our text adventure game world.

    Instance Attributes:
        - id: the id of this location in location data
        - xy_axis: the xy_axis of this location in map
        - name: name of this location
        - short_description: short description of this location
        - long_description: long description of this location
        - available_item: items available in this location

    Representation Invariants:
        - id >= 0
        - name != ""
        - short_description != ""
        - long_deescription != ""

    """
    item_id: int
    xy_axis: list[int]
    name: str
    short_description: str
    long_description: str
    available_items: Optional[list[Item]]
    revisit: bool
    image_file_location: str

    def __init__(self, item_id: int, xy_axis: list[int], name: str, short_description: str, long_description: str,
                 image_file_location: str, available_items: Optional[list[Item]] = None) -> None:
        """Initialize a new location.
        """
        self.item_id = item_id
        self.xy_axis = xy_axis
        self.name = name
        self.short_description = short_description
        self.long_description = long_description
        self.available_items = available_items
        self.revisit = False
        self.image_file_location = image_file_location

        # NOTES:
        # Data that could be associated with each Location object:
        # a position in the world map,
        # a brief description,
        # a long description,
        # a list of available commands/directions to move,
        # items that are available in the location,
        # and whether the location has been visited before.
        # Store these as you see fit, using appropriate data types.
        #
        # This is just a suggested starter class for Location.
        # You may change/add parameters and the data available for each Location object as you see fit.
        #
        # The only thing you must NOT change is the name of this class: Location.
        # All locations in your game MUST be represented as an instance of this class.

    def update_revisited(self) -> None:
        """This function update the revisit state"""
        self.revisit = True


class Player:
    """
    A Player in the text advanture game.

    Instance Attributes:
        - inventory: list of items carried by the player
        - victory: determine if the player passes the game
        - steps_taken: how many steps the player has taken so far
        - curr_location: current location of the player
        - curr_score: current score of the player
        - final_location: the position of exam room
        - mission_completed: whether the player has solved the puzzle

    """

    inventory: list[Item]
    steps_taken: int
    curr_location: list[int]
    max_step: int
    curr_score: float
    final_location: list[int]
    mission_completed: bool

    def __init__(self, x: int, y: int) -> None:
        """
        Initializes a new Player at position (x, y).
        """

        # NOTES:
        # This is a suggested starter class for Player.
        # You may change these parameters and the data available for the Player object as you see fit.

        self.curr_location = [x, y]
        self.inventory = []
        self.steps_taken = 0
        self.max_step = 30
        self.curr_score = 0.0
        self.final_location = [6, 4]
        self.mission_completed = False

    def update_inventory(self, item: Item, action: str) -> None:
        """
        pop the item from inventory if action is drop, append the item if action is take
        """
        if action == 'take':
            self.inventory.append(item)
            if item.can_earn:
                self.update_score(item)
        elif action == "drop":
            self.inventory.remove(item)

    def game_state(self) -> bool:
        """
        check the condition of the game
        """
        if self.curr_location == self.final_location:
            return False
        elif self.steps_taken > self.max_step:
            return False

        return True

    def talk(self, location: list[int], name: str) -> str:
        """
        Talk with the NPC to trigger out extra plot if any of NPCs exists in the location.
        """
        if location == [5, 1] and name == "steve":
            return ("Steve: I just took a ownerless pen and a ownerless sheet and left them at the Help Center. \n"
                    "Feel free to check out if they are yours.")

        elif location == [1, 1] and name == "bob":
            if not self.mission_completed:
                return "Bob: I LOST MY T-CARD! I AM GOING TO SUICIDE!\nYou: ..."
            else:
                return "Bob: Hey my life saver. Enjoy the coffee and good luck on the exam!"
        elif (location == [5, 1] and name != "steve") or (location == [1, 1] and name != "bob"):
            return "nobody here called " + name + '. '
        else:
            return "There is nobody here you can talk with."

    def update_score(self, item: Item) -> None:
        """
        When picking up an item, update player's score based on the score of the item.
        """
        self.curr_score += item.score
        item.can_earn = False

    def print_inventory(self) -> str:
        """
        print out all the items in player's inventory
        """
        return "Your inventory: " + str([item.name for item in self.inventory])

    def check_inventory_by_id(self, item_id: int) -> bool:
        """
        Check whether there exist such an item by item_id.
        """
        for item in self.inventory:
            if item.item_id == item_id:
                return True
        return False


class EventItem(Item):
    """ A special item that can trigger some events when is taken by the player.
    This is a subclass of Item class.
    """

    def __init__(self, name: str, item_id: int, location_x: int, location_y: int, short_description: str,
                 long_description: str, score: float) -> None:
        super().__init__(name, item_id, location_x, location_y, short_description, long_description, score)
        self.can_add = True

    def drop_event_reward2(self, player: Player) -> None:
        """
        player gets extra steps after dropping this item
        """
        print("You bought a cup of coffee using this voucher. Your energy is restored!")
        player.steps_taken -= 5

    def drop_event_reward1(self) -> None:
        """
        player gets another item by dropping this item to NPC
        """
        print('Bob: Thank you for bringing back my TCard! Take this Starbucks voucher as my gift!\n'
              'Starbucks voucher has been added to your inventory')


class World:
    """A text adventure game world storing all location, item and map data.

    Instance Attributes:
        - map: a nested list representation of this world's map
        - items: list of all items
        - location: list of all locations
    """
    items: list[Item]
    locations: list[Location]
    map: list[list]

    def __init__(self, map_data: TextIO, location_data: TextIO, items_data: TextIO) -> None:
        """
        Initialize a new World for a text adventure game, based on the data in the given open files.

        - location_data: name of text file containing location data (format left up to you)
        - items_data: name of text file containing item data (format left up to you)
        """

        # NOTES:

        # map_data should refer to an open text file containing map data in a grid format, with integers separated by a
        # space, representing each location, as described in the project handout. Each integer represents a different
        # location, and -1 represents an invalid, inaccessible space.

        # You may ADD parameters/attributes/methods to this class as you see fit.
        # BUT DO NOT RENAME OR REMOVE ANY EXISTING METHODS/ATTRIBUTES IN THIS CLASS

        # The map MUST be stored in a nested list as described in the load_map() function's docstring below
        self.map = self.load_map(map_data)
        temp_location = self.initialize_location_info(location_data)
        self.locations = []
        for location in temp_location:
            self.locations.append(
                Location(location[0], location[1], location[2], location[3], location[4], location[5]))
        self.items = []
        with open(items_data) as f:
            for line in f:
                new_item = line.split('-')
                self.items.append(
                    Item(new_item[0], new_item[1], new_item[2], new_item[3], new_item[4], new_item[5], new_item[6]))
        event_item_number = 2
        self.initialize_event_item(event_item_number)

        # NOTE: You may choose how to store location and item data; create your own World methods to handle these
        # accordingly. The only requirements:
        # 1. Make sure the Location class is used to represent each location.
        # 2. Make sure the Item class is used to represent each item.

    # NOTE: The method below is REQUIRED. Complete it exactly as specified.
    def load_map(self, map_data: TextIO) -> list[list[int]]:
        """
        Store map from open file map_data as the map attribute of this object, as a nested list of integers like so:

        If map_data is a file containing the following text:
            1 2 5
            3 -1 4
        then load_map should assign this World object's map to be [[1, 2, 5], [3, -1, 4]].

        Return this list representation of the map.
        """
        _my_map = []
        with open(map_data) as f:
            for line in f:
                _my_map.append([int(x) for x in line.split()])
        return _my_map

    # NOTE: The method below is REQUIRED. Complete it exactly as specified.
    def get_location(self, x: int, y: int) -> Optional[Location]:
        """Return Location object associated with the coordinates (x, y) in the world map, if a valid location exists at
         that position. Otherwise, return None. (Remember, locations represented by the number -1 on the map should
         return None.)
        """
        for location in self.locations:
            if location.xy_axis == [x, y]:
                return location
        return None

    def initialize_location_info(self, location_data: TextIO) -> list[list]:
        """
            This is a helper function for initilize location
        """
        with open(location_data) as f:
            location_files = f.readlines()
            _my_all_location_information = []
            temp = ''
            for line in location_files:
                if line == '\n':
                    location_list = temp.split('\n')[0:-1]
                    location_list[0] = int(location_list[0])
                    location_list[1] = [int(i) for i in location_list[1].split(',')]
                    _my_all_location_information.append(location_list)
                    temp = ''
                    continue
                temp += line
        return _my_all_location_information

    def examine(self, name: str, player: Player) -> str:
        """
        print out the long description of an item
        """
        for item in player.inventory:
            if name == item.name:
                return item.long_description

        return 'You do not have such item in your inventory!'
        # for item in self.items:
        #     if item.name == name and item.init_location == player.curr_location:
        #         return item.long_description

    def look(self, player: Player) -> str:
        """
        show the long description of the location and short description of items(if any) in that location
        """
        location_description = ""
        for location in self.locations:
            if location.xy_axis == player.curr_location:
                location_description = location.name + ': ' + location.long_description
                location.revisit = True
                print(climage.convert(location.image_file_location, is_unicode=True, width=120) + "\n")
        item_short_description = "\nItem Available Here:\n"
        for item in self.items:
            if item.curr_location == player.curr_location and item.can_add:
                item_short_description += item.name + ": "
                item_short_description += item.short_description + "\n"
        if item_short_description == "\nItem Available Here:\n":  # nothing is here
            item_short_description += "None\n"

        return location_description + "\n" + item_short_description

    def take(self, name: str, player: Player) -> str:
        """
        take an item and update player's inventory
        """
        for item in self.items:
            if item.curr_location == player.curr_location and item.name == name and item.can_add:
                player.update_inventory(item, "take")
                item.can_add = False
                return "You have take " + item.name + " into your backpack."

        return 'There is no such item can be taken.'

    def drop(self, name: str, player: Player) -> str:
        """
        drop an item and update player's inventory
        """
        voucher = Item
        for voucher_finder in self.items:
            if voucher_finder.name == "voucher":
                voucher = voucher_finder
        # tcard1_index = int
        # for x in range(0, len(self.items)):
        #     if self.items[x].name == 'tcard1':
        #         tcard1_index = x

        if not player.inventory:
            return 'Your inventory is currently empty!'
        for item in player.inventory:
            if (name == item.name and isinstance(item, EventItem) and player.curr_location == [1, 1]
                    and item.item_id == 3):  # T card event
                item.drop_event_reward1()
                player.update_inventory(voucher, "take")
                player.update_inventory(item, "drop")
                player.mission_completed = True
                return "You have dropped " + item.name + "."
            elif (name == item.name and isinstance(item, EventItem) and player.curr_location == [7, 2]
                  and item.item_id == 4):
                # coffee event
                item.drop_event_reward2(player)
                player.update_inventory(item, "drop")
                return "You have dropped " + item.name + "."
            elif name == item.name:
                player.update_inventory(item, "drop")
                item.can_add = True
                item.curr_location = [player.curr_location[0], player.curr_location[1]]
                return "You have dropped " + item.name + "."

        return "There is not such thing you can drop"

    def move(self, direction: str, player: Player) -> str:
        """
            This function move the player according to direction input
        """

        if direction == "north":
            if player.curr_location[0] - 1 >= 0 and \
                    self.map[player.curr_location[0] - 1][player.curr_location[1]] != -1:
                player.curr_location[0] -= 1
                player.steps_taken += 1
                return self.update_position_information(player.curr_location, player)
            else:
                return "It wasn't until you almost crash on wall that you readlize you are heading in wrong direction."
        elif direction == "south":
            if player.curr_location[0] + 1 < len(self.map) and \
                    self.map[player.curr_location[0] + 1][player.curr_location[1]] != -1:
                player.curr_location[0] += 1
                player.steps_taken += 1
                return self.update_position_information(player.curr_location, player)
            else:
                return "It wasn't until you almost crash on wall that you readlize you are heading in wrong direction."
        elif direction == "west":
            if player.curr_location[1] - 1 >= 0 and \
                    self.map[player.curr_location[0]][player.curr_location[1] - 1] != -1:
                player.curr_location[1] -= 1
                player.steps_taken += 1
                return self.update_position_information(player.curr_location, player)
            else:
                return "It wasn't until you almost crash on wall that you readlize you are heading in wrong direction."
        elif direction == "east":
            if player.curr_location[1] + 1 < len(self.map[0]) and \
                    self.map[player.curr_location[0]][player.curr_location[1] + 1] != -1:
                player.curr_location[1] += 1
                player.steps_taken += 1
                return self.update_position_information(player.curr_location, player)
            else:
                return "It wasn't until you almost crash on wall that you readlize you are heading in wrong direction."
        return ''

    def update_position_information(self, curr_position: list[int], player: Player) -> str:
        """
        This function update the position information and item available when player move to a new place.
        """
        for location in self.locations:
            if location.xy_axis == curr_position and location.revisit is False:
                return self.look(player)
            elif location.xy_axis == curr_position:
                return location.name + ": " + location.short_description
        return ''

    def initialize_event_item(self, event_item_count: int) -> None:
        """This method is designed for initializing the eventItem, subclass of item"""
        temp_event_item_list = []
        for _ in range(event_item_count):
            temp_event_item_list.append(self.items.pop())

        for temp in temp_event_item_list:
            self.items.append(EventItem(temp.name, temp.item_id, temp.curr_location[0],
                                        temp.curr_location[1], temp.short_description, temp.long_description,
                                        temp.score))


if __name__ == '__main__':

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (In PyCharm, select the lines below and press Ctrl/Cmd + / to toggle comments.)
    # You can use "Run file in Python Console" to run PythonTA,
    # and then also test your methods manually in the console.
    import python_ta
    python_ta.check_all(config={
        'max-line-length': 120
    })
