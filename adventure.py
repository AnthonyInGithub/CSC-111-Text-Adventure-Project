"""CSC111 Project 1: Text Adventure Game

Instructions (READ THIS FIRST!)
===============================

This Python module contains the code for Project 1. Please consult
the project handout for instructions and details.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 CSC111 Teaching Team
"""
import sys
import game_status
import game_data

basic_info = ("You've got an important exam coming up today, but when you wake up \n"
              "you realize that you have forgotten several important stuffs needed for "
              "your test. \nCan you find those before exam starts?"
              "\nItem needed: Your T-Card, Lucky Pencil, Cheat Sheet")
helper_msg = ("This game is played by type command in the console\n"
                                "Command List:(accept both lower and upper case letter)\n"
                                "north/south/west/east: move north/south/west/east\n"
                                "look: look at stuffs around you\n"
                                "take item_name: take item around you based on item name\n"
                                "examine item_name: take a close look at a specific item\n"
                                "talk person_name: talk to someone base on name")

def determine_action(msg: str) -> str:
    """
    The action in our adventure game can be classified as two kinds.
    1. Action  2. Action + Object
    Base on which action it is, this function determines what will be called
    """
    msg = msg.lower()
    msg = msg.split(" ", 1)
    if len(msg) == 1:
        if msg[0] == "north":
        elif msg[0] == "south":
        elif msg[0] == "west":
        elif msg[0] == "east":
        elif msg[0] == "look":
        elif msg[0] == "exit":  # exit function
            sys.exit()
        elif msg[0] == "help":
            return helper_msg
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
    return ""



if __name__ == "__main__":
    print(basic_info + '\n')

    game_data.World("map.txt", "locations.txt", "items.txt")
    #my_player.determine_action('look')
    while my_status.check_status(current_location):
        input_msg = input("Your Action: ")
        print(determine_action(input_msg))
        print()
        print("Step left: " + str(my_status.get_current_steps_left()))
    """We need a game over comment here"""
    sys.exit()
