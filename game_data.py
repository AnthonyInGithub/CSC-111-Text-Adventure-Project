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

class Item:
    """An item in our text adventure game world.

    Instance Attributes:
        - name: name of the item
        - id: special integer id of the item
        - init_location: where the item initially is
        - short_description: brief description of the item
        - long_description: specific description of the item
        - score: score earn by taking this item
        - can_add: socre can be only earned when item is taken for the first time

    Representation Invariants:
        - # TODO
    """
    name: str
    id: int
    init_location: list[int]
    short_description: str
    long_description: str
    score: float
    can_add: bool

    def __init__(self, name: str, id: int, location_x: int, location_y: int,
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
        self.id = id
        self.init_location = [location_x, location_y]
        self.short_description = short_description
        self.long_description = long_description
        self.score = score
        self.can_add = True


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
    id: int
    xy_axis: list[int]
    name: str
    short_description:str
    long_description: str
    available_items: Optional[list[Item]]
    revisit: bool

    def __init__(self, id:int, xy_axis:list[int], name:str, short_description:str, long_description:str, available_items: Optional[list[Item]] = None) -> None:
        """Initialize a new location.
        """
        self.id = id
        self.xy_axis = xy_axis
        self.name = name
        self.short_description = short_description
        self.long_description = long_description
        self.available_items = available_items
        self.revisit = False
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

    Representation Invariants:
        - # TODO
    """

    inventory: list[Item]
    victory: False
    steps_taken: int
    curr_location: [int]
    max_step: int
    curr_score: float

    def __init__(self, x: int, y: int) -> None:
        """
        Initializes a new Player at position (x, y).
        """

        # NOTES:
        # This is a suggested starter class for Player.
        # You may change these parameters and the data available for the Player object as you see fit.

        self.curr_location = [x, y]
        self.inventory = []
        self.victory = False
        self.max_step = 20
        self.curr_score = 0.0

    def update_inventory(self, item: Item, action: str):
        """
        pop the item from inventory if action is drop, append the item if action is take
        """
        if action == 'take':
            self.inventory.append(item)
            if item.can_add:
                self.update_score(item)
        elif action == "drop":
            self.inventory.remove(item)
        # else:
        #     print()

    def game_win(self) -> bool:
        """
        check condtions for winning the game
        """
        if self.curr_location == [4, 6] and self.steps_taken <= self.max_step:
            required_items = ["Tcard", "Cheat Sheet", "Lucky Pen"]
            carried_items = [item.name for item in self.inventory]
            return all([item in carried_items for item in required_items])

        return False

    def game_lose(self) -> bool:
        """
        check conditions for losing the game
        """
        if self.steps_taken > self.max_step:
            return True
        return False

    def talk(self, location: list[int]) -> None:
        """
        Talk with the NPC to trigger out extra plot if any of NPCs exists in the location.
        """
        if location == [1, 5]:
            print("You: Hi, do you see any of my T-card, cheat sheet, or pen?")
            print("Steve: I did find a pen and a cheat sheet and I just left them in the Help Center.")
        elif location == [1, 1]:
            print("Bob: I LOST MY T-CARD! I AM GOING TO SUICIDE!")
            print("You: ...")
        else:
            print("There is nobody here you can talk with.")

    def update_score(self, item: Item) -> None:
        """
        When picking up an item, update player's score based on the score of the item.
        """
        self.curr_score += item.score
        item.can_add = False

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
        print(temp_location)
        self.locations = []
        for location in temp_location:
            self.locations.append(Location(location[0],location[1],location[2],location[3],location[4]))

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
        for line in open(map_data):
            _my_map.append([int(x) for x in line.split()])
        return _my_map


    # NOTE: The method below is REQUIRED. Complete it exactly as specified.
    def get_location(self, x: int, y: int) -> Optional[Location]:
        """Return Location object associated with the coordinates (x, y) in the world map, if a valid location exists at
         that position. Otherwise, return None. (Remember, locations represented by the number -1 on the map should
         return None.)
        """
        for location in self.locations:
            if location.xy_axis == [x,y]:
                return location
        return None


    def initialize_location_info(self, location_data: TextIO) -> list[list]:
        """
            This is a helper function for initilize location
        """
        location_files = open(location_data).readlines()
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

    def examine(self, name:str, player: Player) -> str:
        for item in player.inventory:
            if name == item.name:
                return item.long_description
        for item in self.items:
            if item.name == name and item.init_location == player.curr_location:
                return item.long_description
    def look(self, player:Player):
        location_description = ""
        for location in self.locations:
            if location.xy_axis == player.curr_location:
                location_description = location.long_description
        item_short_description = ""
        for item in self.items:
            if item.init_location == player.curr_location:
                item_short_description += item.name + ": "
                item_short_description += item.short_description + "\n"

        return location_description +"\n"+ item_short_description
    def take(self, name:str, player:Player) -> str:
        for item in self.items:
            if item.init_location == player.curr_location and item.name == name:
                player.update_inventory(item, "take")
                item.can_add = False
                return "You have take "+item.name+" into your backpack."
    def drop(self, name: str, player:Player):
        for item in player.inventory:
            if name == item.name:
                player.update_inventory(item, "drop")
                item.can_add = True
                item.init_location = player.curr_location
                return "You have drop "+item.name+" ."
