from game import Game
import random

class Hangman(Game):
  messages = {
    'start': 'Ange en bokstav',
    'err': '{value} ser inte ut som en bokstav. Ta en försök till!',
    'intro': 'Spelet HangMan är igång.',
    'startGame': 'Jag har ett hemligt ord, du måste gissa alla bokstäver i det.',
    'win': 'Du har vunnit. Ordet är {secret}',
    'result': '{letter} finns {negation} i secret ord',
    'loose': 'Du har gjort {err} fel gissningar och du har förlorat spelet.',
    'setStart': 'Välj nivå du vill spela på',
    'level': 'Level {levelNumber} {levelName}. du ska ha {err} fel försök',
  }
  words = [
    "hus",
    "katt",
    "hund",
    "äpple",
    "skola",
    "bil",
    "fönster",
    "sommar",
    "vinter",
    "vänskap"
  ]
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

  def __init__(self):
    self.secret = self.getSecret()
    self.errMax = self.setLevel()
    self.attempt = {
      'success': [],
      'miss': [],
    }

  def requestLetter(self):
    while True:
      inp = input(f'{self.messages['start']} ')

      if len(inp) == 1 and inp.isalpha():
        return inp
      else:
        print(self.messages['err'].format(value=inp))

  def isWin(self, attempts, secret):
    for letter in secret:
      if not letter in attempts:
        return False
    return True

  def printAttempts(self, attempts, message):
    print(message)
    print(' '.join(attempts))

  def printErrorCount(self, missAttempts, errMax):
    errCount = len(missAttempts)
    print(
      'Du har gjort ',
      errCount,
      ' fel gissningar. ',
      'Om du gör ',
      errMax - errCount,
      ' fel gissningar mer förlorar du.'
    )

  def getSecret(self):
    return self.words[random.randint(0, len(self.words) - 1)]

  def setLevel(self):
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

  def checkGameStatus(self):
    hasResult = False
    if self.isWin(self.attempt['success'], self.secret):
      print(self.messages['win'].format(secret=self.secret))
      hasResult = True

    if self.errMax == len(self.attempt['miss']):
      print(self.messages['loose'].format(err=self.errMax))
      hasResult = True

    return hasResult
    
  def start(self):
    print(self.messages['intro'])
    print(self.messages['startGame'])

    while True:
      letter = self.requestLetter().lower()
      self.setAttempts(letter)
      self.printAttempts(self.attempt['success'], 'Korrekta försök')
      self.printAttempts(self.attempt['miss'], 'Fel försök')
      self.printErrorCount(self.attempt['miss'], self.errMax)

      if self.checkGameStatus(): return
      print(' ')

# game = Hangman()
# game.start()