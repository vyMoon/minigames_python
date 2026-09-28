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
    for key, game in self.menu.items():
      print(f'{key} - {game['text']}')
      number = int(key)
      if maxIndex < number: maxIndex = number

    return maxIndex

  def start(self):
    while True:
      maxIndex = self.printMenu()
      chosenGame = self.requestNumberBetween(maxIndex)

      if chosenGame == 0:
        print('Spelet avslutas')
        return
      
      game = self.menu[str(chosenGame)]['game']

      if not game: raise ValueError('No game')
      
      game().start()
