import sys
from game_data import World, Player

basic_info = ("You've got an important exam coming up today, but when you wake up \n"
              "you realize that you have forgotten several important stuffs needed for "
              "your test. \nCan you find those before exam starts?"
              "\nItem needed: Your T-Card, Lucky Pencil, Cheat Sheet")
helper_msg = ("This game is played by typing command in the console\n"
              "Command List:(accept both lower and upper case letter)\n"
              "north/south/west/east: move north/south/west/east\n"
              "look: look at stuffs around you\n"
              "take item_name: take item around you based on item name\n"
              "examine item_name: take a close look at a specific item\n"
              "talk person_name: talk to someone base on name\n"
              "exit: quit the game\n"
              "inventory: check your player backpack\n"
              "help: print this helper message again\n"
              "IMPORTANT: FOR THE BEST VISUAL EFFECT, PLEASE ZOOM THE SIZE OF FONT SMALLER AND EXPAND THE CONSOLE\n"
              )
MAX_LENGTH_OF_MSG_PER_LINE = 100

def determine_action(world: World, player: Player, msg: str) -> str:
    """
    The action in our adventure game can be classified as two kinds.
    1. Action  2. Action + Object
    Base on which action it is, this function determines what will be called
    """
    msg = msg.lower()
    msg = msg.split(" ", 1)
    if len(msg) == 1:
        if msg[0] == "north":
            return world.move("north", player)
        elif msg[0] == "south":
            return world.move("south", player)
        elif msg[0] == "west":
            return world.move("west", player)
        elif msg[0] == "east":
            return world.move("east", player)
        elif msg[0] == "look":
            return world.look(player)
        elif msg[0] == "exit":  # exit function
            sys.exit()
        elif msg[0] == "inventory":
            return player.print_inventory()
        elif msg[0] == "help":
            return helper_msg
        elif msg[0] == "score":
            return "Your current score is: " + str(player.curr_score)
        else:
            return "hard to say I recognize this verb."

    else:
        if msg[0] == "take":
            # item.take_object(msg[1])
            return world.take(msg[1], player)
        elif msg[0] == "drop":
            return world.drop(msg[1], player)
        elif msg[0] == "examine":
            return world.examine(msg[1], player)
        elif msg[0] == "talk":
            return player.talk(player.curr_location, msg[1])
        else:
            return "you might just have a typo"


def final_comment(player: Player) -> None:
    """
    Final comment of the game after game lost/win
    """
    if player.steps_taken >= (player.MAX_STEP-1):
        #does not arrive at given step
        print("Just a few steps away, but time has no mercy. You fail to catch up with the exam before it starts.")
    elif player.curr_location == player.FINAL_LOCATION and player.check_inventory_by_id(0) and player.check_inventory_by_id(3) and player.check_inventory_by_id(2) and player.check_inventory_by_id(1):
        #arrive test center with your Tcard, other's Tcard, luck pen, cheat sheet
        print("You catch up the exam. And magic happens. Your Tcard copy itself in your backpack. Now you have two Tcard. Hurrah!")
    elif player.curr_location == player.FINAL_LOCATION and player.check_inventory_by_id(3) and player.check_inventory_by_id(1) and player.check_inventory_by_id(2)\
            and not player.check_inventory_by_id(0):
        #arrive test center with other's Tcard, luck pen, cheat sheet
        print(
            "'Hey, this is not your Tcard, why are you bringing this Tcard to the exam center? What's your purpose?' \nDespite how much you explain, you are accused for academic offense for taking an exam for yourself.")
    elif player.curr_location == player.FINAL_LOCATION:
        # arrive test center without stuff needed
        print("You don't know why you simply go to exam center without stuff you needed. \nI mean, everyone has freedom to do stupid things.")
    elif player.curr_location == player.FINAL_LOCATION and player.check_inventory_by_id(0) and player.check_inventory_by_id(1) and player.check_inventory_by_id(2)\
            and not player.check_inventory_by_id(3):
        # arrive with everything just needed, winning the game
        print("Finding all you need and bring it to exam center on time is tough, but the exam is tougher. \nDespite how much you try, the proof question is far beyond the scope of your ability.\n Is it worthy to try so hard to fail an exam?")

def print_msg_in_limited_letter_per_line(msg: str, max_letter_per_line:int) -> None:
    curr = 0
    last_curr = 0
    line_index = 0
    for i in range(len(msg)):
        curr += 1
        if curr >= max_letter_per_line and msg[i] == " ":
            print(msg[last_curr+line_index*max_letter_per_line:i])
            line_index += 1
            curr -= max_letter_per_line
            last_curr = curr
    print(msg[last_curr+line_index*max_letter_per_line:len(msg)])


if __name__ == "__main__":
    world_system = World("map.txt", "locations.txt", "items.txt")
    player = Player(2, 2)  # set starting location of player; you may change the x, y coordinates here as appropriate
    print(basic_info + '\n')
    print(helper_msg)
    print_msg_in_limited_letter_per_line(world_system.look(player), MAX_LENGTH_OF_MSG_PER_LINE)
    while player.game_state():
        print("What to do? \n")
        choice = input("\nEnter action: ")
        output_msg = determine_action(world_system,player,choice)
        print_msg_in_limited_letter_per_line(output_msg,MAX_LENGTH_OF_MSG_PER_LINE)
        print("Step Left: "+str(player.MAX_STEP-player.steps_taken))
    print()
    final_comment(player)
    print("\nThat's the End of the Game, Thanks for Playing! "+"You Final Score Is: "+str(player.curr_score+player.MAX_STEP-player.steps_taken)+". Feel Free to Try More Ending!")
