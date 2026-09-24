class Tools:
  toolsMessages = {
    'requestNumber':'Ange ett heltal',
    'errorNumber': 'Du har angett {inp} som inte ser ut som ett tal. Ta en till försök!',
    'betweenStart': 'Välj ett tal mellan {min} och {max}',
    'betweenErr': 'talet är inte mellan {min} och {max}. Ta en försök till.',
    'requestLetter': 'Ange en bokstav',
    'errLetter': '{value} ser inte ut som en bokstav. Ta en försök till!',
  }
  def requestNumber(self):
    while True:
      inp = input(f'{self.toolsMessages["requestNumber"]} ')
      try:
        number = int(inp)
        return number
      except:
        print(self.toolsMessages['errorNumber'].format(inp=inp))
        continue
  
  def requestNumberBetween(self, max, min = 0):
    print(self.toolsMessages['betweenStart'].format(min=min, max=max))
  
    while True:
      number = self.requestNumber()
      if number > max or number < min:
        print(self.toolsMessages['betweenErr'].format(min=min, max=max))
        continue
      return number

  def requestLetter(self):
    while True:
      inp = input(f'{self.toolsMessages['requestLetter']} ')
  
      if len(inp) == 1 and inp.isalpha():
        return inp
      else:
        print(self.toolsMessages['errLetter'].format(value=inp))

  def wordsDeclension(self, amount, word, suffix, removeLast = False):
    if amount == 0 or amount > 1:
      response = word[0: -1] if removeLast else word
      response += suffix
      return response
  
    return word
