class Player:

    """
    The purpose of this Class is to hold values that the user will use during the gameplay, those values are the letter that he/she choses and the parachute from which the lines will be removed if the user fails to guess a specific letter.
    """

    def __init__(self):
        # This constructor without arguments initializes to None this Class' attributes
        self._chosen_letter = None
        self._parachute = None

    def get_chosen_letter(self):
        # We retrieve the value of the chosen letter
        return self._chosen_letter

    def set_chosen_letter(self, chosen_letter):
        # We assign a new value to the chosen letter
        self._chosen_letter = chosen_letter

    def get_parachute(self):
        # We retrieve the value of the parachute
        return self._parachute

    def set_parachute(self, parachute):
        # We assign a new value to the parachute
        self._parachute = parachute
