def rpc():
import random
  inp = input('Enter your input')
  sys_score = 0
  you_score = 0
  draw = 0
  #result = ''
  while inp.lower() != 'quit':
    
    result = ''
    choices = ['rock', 'paper', 'scissors']
    #inp = input('Enter your input')

    sys_choice_index = random.randint(0, len(choices) - 1)
    sys_choice = choices[sys_choice_index]
    print(f'sys_choice: {sys_choice}')

    if inp.lower() == sys_choice:
      result = 'Draw'
      draw += 1
      print(result)

    elif inp.lower() == 'rock' and sys_choice == 'scissors':
      result = 'You won'
      you_score += 1
      print(result)


    elif inp.lower() == 'scissors' and sys_choice == 'rock':
      result = 'You loose'
      sys_score += 1
      print(result)

    elif inp.lower() == 'rock' and sys_choice == 'paper':
      result = 'You loose'
      sys_score += 1
      print(result)

    elif inp.lower() == 'paper' and sys_choice == 'rock':
      result = 'You win'
      you_score += 1
      print(result)

    elif inp.lower() == 'scissors' and sys_choice == 'paper':
      result = 'You won'
      you_score += 1
      print(result)

    elif inp.lower() == 'paper' and sys_choice == 'scissors':
      result = 'You loose'
      sys_score += 1
      print(result)

    inp = input('Enter your input')

  print(f'sys_score: {sys_score}')
  print(f'you_score: {you_score}')
  print(f'draw: {draw}')


#print(result)

rpc()