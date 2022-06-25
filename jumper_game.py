import random
from word import Word
from player import Player
from game import Game
from formatter import Formatter

# We draw a parachute
PARACHUTE = [
    "  ___  ",
    " /___\\",
    " \   / ",
    "  \ /  ",
    "   0   ",
    "  /|\\ ",
    "  / \\ ",
    "       ",
    "^^^^^^^"
]

WORDS = ["clean", "organize", "teach", "sudent", "television", "airplane"]

PERSON_HEAD_INDEX = 5


def main():
    # We randomly choose a word from a word list
    chosen_word = random.choice(WORDS)

    # We will utilize the methods from a Formatter helper
    formatter = Formatter()

    # The word is hidden with underscore
    hidden_word = formatter.create_hidden_word(chosen_word)

    # We create a Word object with the readable word, as well as with the hidden word
    word = Word(chosen_word, hidden_word)

    # We create a Player to assign him/her the parachute as well as the letter chosen by himself/herself
    player = Player()
    player.set_parachute(PARACHUTE)

    # We create a Game object to hold the boolean values to continue or stop the game
    game = Game()
    # By default we are allowed to start the game
    while game.get_continue_playing():
        # By default we have to validate if the letter entered needs to be validated to meet certain conditions
        game.set_validate_letter(True)
        while game.get_validate_letter():

            # We ask the user to enter a letter
            player.set_chosen_letter(
                input(f"Guess a letter [a-z]: ").lower())

            # We require the letter to be of only 1 character and we prevent the player to enter a repeated letter
            if len(player.get_chosen_letter()) == 1 and not player.get_chosen_letter().isdigit() and player.get_chosen_letter() not in word.get_hidden_word() and player.get_chosen_letter().isalpha():
                game._validate_letter = False
            elif player.get_chosen_letter() in word.get_hidden_word() and len(player.get_chosen_letter()) == 1:
                print(
                    "Please enter a letter that you have not entered before [a-z]")
            else:
                print("Please enter a valid letter [a-z]")

        # The correctly guessed words are shown, and the rest remains hidden
        complete_word = ""
        if player.get_chosen_letter() in word.get_word():
            index = 0
            for letter in word.get_word():
                if letter == player.get_chosen_letter():
                    complete_word += letter
                else:
                    complete_word += word.get_hidden_word()[index:index+1]
                index += 1
            word.set_hidden_word(complete_word)
        else:
            # If the letter is not found in the word we proceed to remove the upper line of text of the parachute
            player.get_parachute().pop(0)

        # We validate if the head of the person in the parachute is reached, so we can end the game
        if len(player.get_parachute()) <= PERSON_HEAD_INDEX:
            player.get_parachute()[0] = "   x   "
            formatter.print_list(player.get_parachute())
            game.set_continue_playing(False)
            return

        # We prepare the hidden word to be printed, we add spaces between its characters
        separated_text = formatter.separate_hidden_text(word.get_hidden_word())
        print(separated_text)

        # We print the parachute
        formatter.print_list(player.get_parachute())

        # If the character underscore is in the hidden word, it means that we can cntinue guessing
        if "_" not in word.get_hidden_word():
            print("You win!")
            return


if __name__ == "__main__":
    main()
