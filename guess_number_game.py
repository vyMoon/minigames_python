import random
from tools import Tools

class GuessNumberGame(Tools):
  messages = {
    'intro': 'Gissa talet är igång',
    'win': 'Bra jobbat! Talet {number} är correct!',
    'count': 'Du gjorde {attempt} försök att gissa.',
    'notWin': 'Talet {number} är för {comparison}. Ta en försök till!',
    'start': 'Jag har ett hemligt tal. Gissa det. Gör så få försök som möjligt!',
    'setStart': 'Välj vilken nivå du vill spela på',
    'setLevel': 'Nivå {levelNumber} {levelName}. Tal ligger mellan {min} och {max}',
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
    '3': {
      'name': 'Extrem',
      'max': 1000000
    }
  }
  minNumber = 0

  def __init__(self):
    self.attemptCounter = 0

  def start(self):
    print(self.messages['intro'])
    self.secret = self.getSecret(
      self.getLevel()
    )
    print(self.messages['start'])
    self.runGame()
  
  def runGame(self):
    while True:
      self.attemptCounter += 1
      number = self.requestNumber()

      if number == self.secret:
        print('\n')
        print(self.messages['win'].format(number=number))
        print(self.messages['count'].format(attempt=self.attemptCounter), '\n')
        return
      else:
        comparison = 'högt' if number > self.secret else 'lågt'
        print(self.messages['notWin'].format(number= number, comparison=comparison))


  def printLevels(self):
    for index, level in self.levels.items():
      print(self.messages['setLevel'].format(
        levelNumber=index, 
        levelName=level['name'], 
        min=self.minNumber, 
        max=level['max'])
      )

  def getMaxLevelKey(self):
    max = 0
    for key in self.levels.keys():
      number = int(key)
      if max < number: max = number
    return max

  def getSecret(self, chosenLevel):
    return random.randint(
      self.minNumber,
      self.levels[str(chosenLevel)]['max']
    )

  def getLevel(self):
    print(self.messages['setStart'], '\n')
    self.printLevels()
    print('\n')

    chosenLevel = self.requestNumberBetween(
      self.getMaxLevelKey()
    )
    return chosenLevel

# game = GuessNumberGame()
# game.start()
