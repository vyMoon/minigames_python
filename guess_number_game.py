import random
from game import Game

class GuessNumberGame(Game):
  messages = {
    'win': 'Bra jobbat! Talet {number} är correct!',
    'count': 'Du gjorde {attempt} försök att gissa.',
    'notWin': 'Talet {number} är för {comparison}. Ta en försök till!',
    'start': 'Jag har ett hemligt tal. Gissa det. Gör så få försök som möjligt!',
    'setStart': 'Välj nivå du vill spela på',
    'setLevel': 'Level {levelNumber} {levelName}. Tal ligger mellan {min} och {max}',
  }
  levels = {
    '0': {
      'name': 'Enkel',
      'max': 10,
    },
    '1': {
      'name': 'Normal',
      'max': 100,
    },
    '2': {
      'name': 'Hård',
      'max': 1000,
    },
  }
  minNumber = 0

  def __init__(self):
    self.correctNumber = self.setLevel()
    self.attemptCounter = 0

  def start(self):
    print(self.messages['start'])
    while True:
      self.attemptCounter += 1
      number = self.requestNumber()

      if number == self.correctNumber:
        print(self.messages['win'].format(number=number))
        print(self.messages['count'].format(attempt=self.attemptCounter))
        return
      else:
        comparison = 'högt' if number > self.correctNumber else 'lågt'
        print(self.messages['notWin'].format(number= number, comparison=comparison))

  def setLevel(self):
    maxLevel = 0

    print(self.messages['setStart'])

    for index, level in self.levels.items():
      print(self.messages['setLevel'].format(
        levelNumber=index, 
        levelName=level['name'], 
        min=self.minNumber, 
        max=level['max'])
      )
      num = int(index)
      if maxLevel < num: maxLevel = num
    
    chosenLevel = self.requestNumberBetween(maxLevel)
    return random.randint(self.minNumber, self.levels[str(chosenLevel)]['max'])

# game = GuessNumberGame()
# game.start()
