import sys

import world
import game_status


# import item


class Player:
    """This is the player class of the game. It determines what action will be
    done based on the input
    """
    world_system: world.World
    _helper_message: str
    status_system: game_status.GameStatus

    # _item_system: Item
    def __init__(self):
        self.world_system = world.World()
        self.status_system = game_status.GameStatus()
        self._helper_message = ("This game is played by type command in the console\n"
                                "Command List:(accept both lower and upper case letter)\n"
                                "north/south/west/east: move north/south/west/east\n"
                                "look: look at stuffs around you\n"
                                "take item_name: take item around you based on item name\n"
                                "examine item_name: take a close look at a specific item\n"
                                "talk person_name: talk to someone base on name")

    def determine_action(self, msg: str) -> str:
        """
        The action in our adventure game can be classified as two kinds.
        1. Action  2. Action + Object
        Base on which action it is, this function determines
        """
        msg = msg.lower()
        msg = msg.split(" ", 1)
        if len(msg) == 1:
            if msg[0] == "north":
                self.status_system.update_step()
                return self.world_system.move_north()
            elif msg[0] == "south":
                self.status_system.update_step()
                return self.world_system.move_south()
            elif msg[0] == "west":
                self.status_system.update_step()
                return self.world_system.move_west()
            elif msg[0] == "east":
                self.status_system.update_step()
                return self.world_system.move_east()
            elif msg[0] == "look":
                return self.world_system.show_position_information()
            elif msg[0] == "exit":  # exit function
                sys.exit()
            elif msg[0] == "help":
                return self._helper_message
            else:
                return "hard to say I recognize this verb"

        else:
            if msg[0] == "take":
                # item.take_object(msg[1])
                pass
            elif msg[0] == "drop":
                pass
            elif msg[0] == "examine":
                pass
            elif msg[0] == "talk":
                pass
            else:
                return "you might just have a typo"

    def game_start_info(self):
        """This function run and display current location information to the player,"""
        return self.world_system.show_position_information()
