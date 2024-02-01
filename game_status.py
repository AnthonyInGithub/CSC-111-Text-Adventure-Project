
class GameStatus:
    """This class control the game status. There are 2 status of game. started, finished.
        The transition of game status is determined by the movement steps.

        IMPORTANT:
        THIS IS A STATIC CLASS THAT DOESN'T NEED TO BE INITIALIZE

        Instance Attributes:
            - steps: This is how many step did play take
            - game_run_status: True-started, False-finished
            - MAX_STEP: the maximum number of step player can take
            - DESTINATION_POSITION: destination's xy position
    """
    _step = 0
    _game_run_status = True
    _MAX_STEP = 5
    _DESTINATION_POSITION = [6, 4]

    @staticmethod
    def check_status(locationXY:list)->bool:
        """
        This is the update function called on every move. It checks the location and steps to
        determine the current game status

        Instance Attribute:
            - locationXY: current player location
        """
        if GameStatus._step >= GameStatus._MAX_STEP:
            _game_run_status = False
        if GameStatus.check_destination_arrival(locationXY):
            GameStatus._game_run_status = False
        # needs inventory system here

        return GameStatus._game_run_status

    @staticmethod
    def get_current_steps_left():
        """This function return steps left"""
        return GameStatus._MAX_STEP - GameStatus._step

    @staticmethod
    def get_game_over_comment(locationXY:list) -> str:
        """This function determines what's final comment based on win or lost
        Instance Attribute:
            - locationXY: current player location
        """
        if GameStatus.check_destination_arrival(locationXY):  # XY of test room. Check game design document for full XY correspondent list.
            return "Congra, pass"
        else:
            return "ohh, you didn't arrive at the given step with everything you need"

    @staticmethod
    def check_destination_arrival(locationXY: list) -> bool:
        """
        This function check whether the player is at the destination or not
        """
        return locationXY == GameStatus._DESTINATION_POSITION

    @staticmethod
    def update_step():
        """This function update the step"""
        GameStatus._step += 1

    @staticmethod
    def increase_steps_on_coffee_event():
        """This functions give player more step when player complete a specific event"""
        GameStatus._step -= 3
