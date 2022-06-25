class Game:

    """
    The purpose of this Class is to hold the boolean values that allow the user to end up or start the game.
    """

    def __init__(self):
        # This constructor without arguments initializes to True this Class' attributes because this allows the Game to start when these values are used
        self._continue_playing = True
        self._validate_letter = True

    def get_continue_playing(self):
        # We retrieve the value of the attribute _continue_playing to allow the game to stop or to continue
        return self._continue_playing

    def set_continue_playing(self, continue_playing):
        # We assign a new value to the attribute _continue_playing to allow the game to stop or to continue
        self._continue_playing = continue_playing

    def get_validate_letter(self):
        # We retrieve the value of the letter to validate
        return self._validate_letter

    def set_validate_letter(self, validate_letter):
        # We assign a new value to the letter to validate
        self._validate_letter = validate_letter

    
