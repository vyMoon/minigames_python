from hangman_game import Hangman
from guess_number_game import GuessNumberGame
from tools import Tools
from menu import Menu

menu = Menu(Hangman, GuessNumberGame)
menu.start()
