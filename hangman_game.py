from tools import Tools
from hangman_words import words
import random

class Hangman(Tools):
  messages = {
    'intro': 'Spelet HangMan är igång.',
    'startGame': 'Jag har ett hemligt ord, du måste gissa alla bokstäver i det.',
    'win': 'Du har vunnit. Ordet är {secret}',
    'result': '{letter} finns {negation} i secret ord',
    'lose': 'Du har gjort {err} fel gissningar, och du har förlorat spelet.',
    'setStart': 'Välj vilken nivå du vill spela på',
    'level': 'Level {levelNumber} {levelName}. du ska ha {err} fel försök',
  }
  levels = {
    '0': {
      'name': 'Enkel',
      'err': 30,
    },
    '1': {
      'name': 'Normal',
      'err': 15,
    },
    '2': {
      'name': 'Hård',
      'err': 5,
    },
  }
  words = words

  def __init__(self):
    self.secret = self.getSecret()
    self.attempt = {
      'success': [],
      'miss': [],
    }

  def getSecret(self):
    return self.words[
      random.randint(0, len(self.words) - 1)
    ]

  def start(self):
    print(self.messages['intro'])
    self.errMax = self.getLevel()
    print(self.messages['startGame'])
  
    while True:
      letter = self.requestLetter().lower()
      self.setAttempts(letter)
      self.printAttempts(self.attempt['success'], 'Korrekta försök')
      self.printAttempts(self.attempt['miss'], 'Fel försök')
      self.printErrorCount(self.attempt['miss'], self.errMax)
  
      if self.checkGameStatus(): return
      print('\n')

  def getLevel(self):
    maxLevel = 0

    print(self.messages['setStart'])

    for index, level in self.levels.items():
      print(self.messages['level'].format(
        levelNumber=index, 
        levelName=level['name'],
        err=level['err'])
      )

      num = int(index)
      if maxLevel < num: maxLevel = num
    
    chosenLevel = self.requestNumberBetween(maxLevel)
    return self.levels[str(chosenLevel)]['err']

  def setAttempts(self, letter):
    message = ''
    if letter in self.secret:
      self.attempt['success'].append(letter)
      message = self.messages['result'].format(letter=letter, negation='')
    else:
      self.attempt['miss'].append(letter)
      message = self.messages['result'].format(letter=letter, negation='inte')
    print(message)

  def printAttempts(self, attempts, message):
    print(message)
    print(' '.join(attempts))

  def printErrorCount(self, missAttempts, errMax):
    errCount = len(missAttempts)
    errLeft = errMax - errCount
    if errLeft > 0:
      print(
        f'Du har gjort {errCount}',
        self.wordsDeclension(errCount, 'felaktig', 'a'),
        self.wordsDeclension(errCount, 'gissning', 'ar'),
        'Om du gör',
        errLeft,
        self.wordsDeclension(errLeft, 'felaktig', 'a'),
        self.wordsDeclension(errLeft, 'gissning', 'ar'),
        'mer förlorar du.'
      )

  def checkGameStatus(self):
    hasResult = False
    if self.isWin(self.attempt['success'], self.secret):
      print(self.messages['win'].format(secret=self.secret))
      hasResult = True

    if self.isLose():
      print(self.messages['lose'].format(err=self.errMax))
      hasResult = True

    return hasResult

  def isWin(self, attempts, secret):
    for letter in secret:
      if not letter in attempts:
        return False
    return True

  def isLose(self):
      return self.errMax == len(self.attempt['miss'])

# game = Hangman()
# game.start()