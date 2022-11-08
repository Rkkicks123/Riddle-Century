import time


star='*'*4
print (star+'Hi and welcome to my game'+star)
def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)

#Intro
name = text_prompt('What is your name ')
print(str("It's lovely to meet you, ") + name)
Riddle1 = True
Riddle2 = True


#GameCode
def getYesOrNo():
  firstLetter = text_prompt('Yes or no?')[0].upper()
  answer = None
  if firstLetter == 'Y':
    answer = True
  elif firstLetter == 'N':
    answer = False
  else:
    print('Please answer Yes or No')
    answer = getYesOrNo()
  return answer
  
  
  #####Riddle's
def Riddle1Question():
  print('I Have a question, you are in a life and death sitution where there are two doors, one door has lions who have not eaten for a few days, the next door has magnify glasses that can burn you! What door wiill you choose? Your guess:')


def Riddle1Answer():
  user = input()
  if user == 'Magify Glasses' or user == 'magnify glasses' or user == 'm' or user == 'M' or user == 'magnifying glasses' or user == 'magnifying glass' or user == 'Magnifying glasses' or user == 'Magnifying glass':
      print(''.join([str(x) for x in [user, ' is correct, Alive, ', name]]))
      print (star+'Nice job, next Riddle :)'+star)
      time.sleep (2)
      time.sleep (2)
      Riddle2Question()
      Riddle2Answer()
  else:
      print(''.join([str(x) for x in [user, ' is not correct, dead, ', name]]))
      print('Would you like to try again? Spelling or caplitization could be at fault')
      getYesOrNo()
      Riddle1Question()
  return Riddle1Answer()

def Riddle2Question():
  print ('''David's father has three sons : Snap, Crackle and _____ ?''')

def Riddle2Answer():
  user = input()
  if user == 'David' or user == 'david' or user == "David's"  or user == 'Davids'  or user == "david's"  or user == 'davids' or user == 'd' or user == 'D':
      print(''.join([str(x) for x in [user, ' is correct, ', name]]))
      print (star+'Nice job, next Riddle :)'+star)
      time.sleep (2)
      time.sleep (2)
      Riddle3Question()
      Riddle3Answer()
  else:
      print(''.join([str(x) for x in [user, ' is not correct, ', name]]))
      print('Would you like to try again? Spelling or caplitization could be at fault')
      getYesOrNo()
      Riddle2Question()
  return Riddle2Answer()

def Riddle3Question():
  print('What is black when you buy it, red when you use it, and gray when you throw it away?')

def Riddle3Answer():
  user = input()
  if user == 'Charcoal' or user == 'charcoal':
      print(''.join([str(x) for x in [user, ' is correct, ', name]]))
      print (star+'Nice job, next Riddle :)'+star)
      time.sleep (2)
      time.sleep (2)
      Riddle4Question()
      Riddle4Answer()
     
  else:
      print(''.join([str(x) for x in [user, ' is not correct, ', name]]))
      print('Would you like to try again? Spelling or caplitization could be at fault')
      getYesOrNo()
      Riddle3Question()
  return Riddle3Answer()

def Riddle4Question():
  print('How much dirt is there in a hole that measures two feet by three feet by four feet?')

def Riddle4Answer():
  user = input()
  if user == 'No Dirt' or user == 'no dirt' or user == 'none' or user == 'None' or user == '0':
      print(''.join([str(x) for x in [user, ' is correct, ', name]]))
      print (star+'Nice job, next Riddle :)'+star)
      time.sleep (2)
      time.sleep (2)
      Riddle5Question()
      Riddle5Answer()
  else:
      print(''.join([str(x) for x in [user, ' is not correct, ', name]]))
      print('Would you like to try again? Spelling or caplitization could be at fault')
      getYesOrNo()
      Riddle4Question()
  return Riddle4Answer()

def Riddle5Question():
  print('What can run but never walks, has a mouth but never talks, has a head but never weeps, has a bed but never sleeps?')

def Riddle5Answer():
  user = input()
  if user == 'a River' or user == 'A River' or user == 'a river' or user == 'A river' or user == 'River' or user == 'river':
      print(''.join([str(x) for x in [user, ' is correct, ', name]]))
      print('Thank you for playing. Have a great day :)')
  else:
      print(''.join([str(x) for x in [user, ' is not correct, ', name]]))
      print('Would you like to try again? Spelling or caplitization could be at fault')
      getYesOrNo()
      Riddle4Question()
  return Riddle4Answer()

def runGame():
  Riddle1Question()
  Riddle1Answer()

  
  
###RunningGame
runGame()