class World:
    """
    This class controls the player's location and description of location in the game
    """
    _current_position: list[int]
    _my_map: list[list[int]]
    _my_all_location_information: list[list]
    _position_been: list[list]

    def __init__(self):
        """Init current location, map, and location information"""
        self._current_position = [2, 2]
        self._my_map = []
        self._position_been = []
        for line in open(r'map.txt'):
            self._my_map.append([int(x) for x in line.split()])
        self.initialize_location_info()

    def move_north(self) -> str:
        """
            call this function will make character move to the north. If the north is not available,
            return wrong movement information. Otherwise, print location's description.
        """
        if (self._current_position[0] - 1) >= 0 and \
                self._my_map[self._current_position[0] - 1][self._current_position[1]] != -1:
            self._current_position[0] -= 1
            return self.update_position_information(self._current_position)
        else:
            return self.wrong_movement_information()

    def move_south(self) -> str:
        """
            call this function will make character move to the south. If the south is not available,
            return wrong movement information. Otherwise, print location's description.
        """
        if (self._current_position[0] + 1) < len(self._my_map) and \
                self._my_map[self._current_position[0] + 1][self._current_position[1]] != -1:
            self._current_position[0] += 1
            return self.update_position_information(self._current_position)
        else:
            return self.wrong_movement_information()

    def move_west(self) -> str:
        """
            call this function will make character move to the west. If the west is not available,
            return wrong movement information. Otherwise, print location's description.
        """
        if (self._current_position[1] - 1) >= 0 and \
                self._my_map[self._current_position[0]][self._current_position[1] - 1] != -1:
            self._current_position[1] -= 1
            return self.update_position_information(self._current_position)
        else:
            return self.wrong_movement_information()

    def move_east(self) -> str:
        """
            call this function will make character move to the east. If the east is not available,
            return wrong movement information. Otherwise, print location's description.
        """
        if (self._current_position[1] + 1) < len(self._my_map[0]) and \
                self._my_map[self._current_position[0]][self._current_position[1] + 1] != -1:
            self._current_position[1] += 1
            return self.update_position_information(self._current_position)
        else:
            return self.wrong_movement_information()

    def get_player_current_location_on_xy_axis(self) -> list[int]:
        """
        This function returns the player_current_location by [x,y]
        """
        return self._current_position

    def update_position_information(self, position: list) -> str:
        """
        This function update the location description when you move to somewhere. If you have
        move to a same place twice, at the second time, it will only show short description.

        Instance Attribute:
            position: current position after moved
        """
        for location in self._my_all_location_information:
            if location[1][0] == self._current_position[0] and location[1][1] == self._current_position[1]:
                if position in self._position_been:
                    return location[3]
                else:
                    return location[2]
        return "Doesn't exist such location"

    def show_position_information(self) -> str:
        """This function will return the long description of current location information"""
        for location in self._my_all_location_information:
            if location[1][0] == self._current_position[0] and location[1][1] == self._current_position[1]:
                return location[3]
        return 'doesn'

    def wrong_movement_information(self) -> str:
        """
        This function return the wrong movement message
        """
        return "It was until you almost crash on wall that you realize there is not way through"

    def initialize_location_info(self) -> None:
        """
            This is a helper function for initilize location
        """
        location_files = open('locations.txt').readlines()
        self._my_all_location_information = []
        temp = ''
        for line in location_files:
            if line == '\n':
                location_list = temp.split('\n')[0:-1]
                location_list[0] = int(location_list[0])
                location_list[1] = [int(i) for i in location_list[1].split(',')]
                self._my_all_location_information.append(location_list)
                temp = ''
                continue
            temp += line
