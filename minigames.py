from hangman_game import Hangman
from guess_number_game import GuessNumberGame
from tools import Tools

class Menu(Tools):
  def __init__(self, hangman, guessNumberGame):
    self.menu = {
      '0': {
        'text': 'Avsluta',
        'game': None,
      },
      '1': {
        'text': 'Gissa numret spel',
        'game': guessNumberGame,
      },
      '2': {
        'text': 'Hangman',
        'game': hangman,
      }
    }

  def printMenu(self):
    print('Menu')
    maxIndex = 0
    for index, game in self.menu.items():
      print(f'{index} - {game['text']}')
      number = int(index)
      if maxIndex < number: maxIndex = number

    return maxIndex

  def start(self):
    while True:
      maxIndex = self.printMenu()
      chosen = self.requestNumberBetween(maxIndex)

      if chosen == 0:
        print('Spelet avslutas')
        return
      else:
        game = self.menu[str(chosen)]['game']()
        game.start()

menu = Menu(Hangman, GuessNumberGame)
menu.start()