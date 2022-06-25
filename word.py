class Word:
    """
    This Class allows us to hold a word chosen by a user with and without hidding its characters. so we can show a word hidden but also being able to get the complete readable word.
    """

    def __init__(self):
        # This constructor without arguments initializes to None this Class' attributes
        self._word = None
        self._hidden_word = None

    def __init__(self, word, hidden_word):
        # This constructor receives two arguments, the first is the readable word and the second argument is the hidden word
        self._word = word
        self._hidden_word = hidden_word

    def get_word(self):
        # We retrieve the value of the readable word
        return self._word

    def set_word(self, word):
        # We assign a new value to the readable word
        self._word = word

    def get_hidden_word(self):
        # We retrieve the value of the hidden word
        return self._hidden_word

    def set_hidden_word(self, hidden_word):
        # We assign a new value to the hidden word
        self._hidden_word = hidden_word
