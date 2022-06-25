class Formatter:

    """
    The purpose of this Class is to be a helper in the Jumper Game by formatting and printing text that is required during the gameplay.
    """

    def __init__(self):
        return

    def print_list(self, list):
        # We print each element of a list in a separate line
        for line in list:
            print(line)

    def separate_hidden_text(self, text):
        # A space is added between the letters of the text entered
        hidden_text = ""
        for letter in text:
            hidden_text += letter + " "

        return hidden_text.strip()

    def create_hidden_word(self, word):
        # A new text is generated containing only underscore characters, its size is equals to the size of the entered text
        hidden_text = ""
        for _ in range(0, len(word)):
            hidden_text += "_"

        return hidden_text.strip()
