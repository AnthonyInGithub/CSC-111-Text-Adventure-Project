import world


# import inventory

class GameStatus:
    """This class control the game status. There are 2 status of game. started, finished.
        The transition of game status is determined by the movement steps.

        Instance Attributes:
            - steps: This is how many step did play take
            - game_run_status: True-started, False-finished
            - MAX_STEP: the maximum number of step player can take
            - DESTINATION_POSITION: destination's xy position
    """
    _step: int
    _game_run_status: bool
    _MAX_STEP: int
    _DESTINATION_POSITION: list

    def __init__(self):
        """
        Initialize the game status, settle down max_step
        """
        self._step = 0
        self._game_run_status = True
        self._MAX_STEP = 5
        self._DESTINATION_POSITION = [6, 4]

    def check_status(self, locationXY:list)->bool:
        """
        This is the update function called on every move. It checks the location and steps to
        determine the current game status

        Instance Attribute:
            - locationXY: current player location
        """
        if self._step >= self._MAX_STEP:
            self._game_run_status = False
        if self.check_destination_arrival(locationXY):
            self._game_run_status = False
        # needs inventory system here

        return self._game_run_status

    def get_current_steps_left(self):
        """This function return steps left"""
        return self._MAX_STEP - self._step

    def get_game_over_comment(self, locationXY:list) -> str:
        """This function determines what's final comment based on win or lost
        Instance Attribute:
            - locationXY: current player location
        """
        if self.check_destination_arrival(locationXY):  # XY of test room. Check game design document for full XY correspondent list.
            return "Congra, pass"
        else:
            return "ohh, you didn't arrive at the given step with everything you need"
    def check_destination_arrival(self, locationXY: list):
        """
        This function check whether the player is at the destination or not
        """
        return locationXY == self._DESTINATION_POSITION
    def update_step(self):
        """This function update the step"""
        self._step += 1

    def increase_steps_on_coffee_event(self):
        """This functions give player more step when player complete a specific event"""
        self._step -= 3
