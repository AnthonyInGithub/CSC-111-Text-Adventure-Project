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

import player

basic_info = ("You've got an important exam coming up today, but when you wake up \n"
              "you realize that you have forgotten several important stuffs needed for "
              "your test. \nCan you find those before exam starts?"
              "\nItem needed: Your T-Card, Lucky Pencil, Cheat Sheet")

if __name__ == "__main__":
    my_player = player.Player()
    print(basic_info + '\n')
    my_status = my_player.status_system
    print(my_player.game_start_info())
    while my_status.check_status(my_player.world_system.get_player_current_location_on_xy_axis()):
        input_msg = input("Your Action: ")
        print(my_player.determine_action(input_msg))
        print()
        print("Step left: " + str(my_status.get_current_steps_left()))
    print(my_status.get_game_over_comment(my_player.world_system.get_player_current_location_on_xy_axis()))
    sys.exit()
