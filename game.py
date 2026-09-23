class Game:
  numberMessages = {
    'requestNumber':'Ange ett heltal',
    'errorNumber': 'Du har angett {inp} som inte ser ut som ett tal. Ta en till försök!',
    'betweenStart': 'Välj ett tal mellan {min} och {max}',
    'betweenErr': 'talet är inte mellan {min} och {max}. Ta en försök till.',
  }
  def requestNumber(self):
    while True:
      inp = input(f'{self.numberMessages["requestNumber"]} ')
      try:
        number = int(inp)
        return number
      except:
        print(self.numberMessages['errorNumber'].format(inp=inp))
        continue
  
  def requestNumberBetween(self, max, min = 0):
    print(self.numberMessages['betweenStart'].format(min=min, max=max))
  
    while True:
      number = self.requestNumber()
      if number > max or number < min:
        print(self.numberMessages['betweenErr'].format(min=min, max=max))
        continue
      return number