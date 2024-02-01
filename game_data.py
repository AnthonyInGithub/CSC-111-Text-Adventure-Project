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

    def __init__(self, id:int, xy_axis:list[int], name:str, short_description:str, long_description:str, available_items: Optional[list[Item]]) -> None:
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




class World:
    """A text adventure game world storing all location, item and map data.

    Instance Attributes:
        - map: a nested list representation of this world's map
        - items: list of all items
        - location: list of all locations
    """
    #items: list[Item]
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
