def randomPasswordGenerator(length):
  import random 
  lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

  uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

  special_characters = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+',
                       ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@',
                       '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

  digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

  #Decide how many chatacters to choose from which list
  if length < 12:
    length += 10
  if length % 4 == 0:
    n_lowercase = length//4
    n_uppercase = length // 4
    n_special_characters = length // 4
    n_digits = length // 4
   # print( n_digits,n_lowercase,n_uppercase, n_special_characters)

  else:
    n_lowercase = length//4
    n_uppercase = length // 4
    n_special_characters = length // 4
    n_digits = length - n_lowercase * 3
    
    #print(n_digits,n_lowercase,n_uppercase, n_special_characters)
  
  #Choosing random characters from the lists

  #lowercase
  selected_lowercase = []
  for i in range(1, n_lowercase+1):
    k = random.randint(1, len(lowercase) -1)
    selected_lowercase.append(lowercase[k])
  print(selected_lowercase)

  #uppercase
  selected_uppercase = []
  for i in range(1, n_uppercase+1):
    k = random.randint(1, len(uppercase) -1)
    selected_uppercase.append(uppercase[k])
  print(selected_uppercase)

  #special_characters
  selected_special_characters = []
  for i in range(1, n_special_characters + 1):
    k = random.randint(1, len(special_characters)-1)
    selected_special_characters.append(special_characters[k])
  print(selected_special_characters)

  #digits
  selected_digits = []
  for i in range(1, n_digits +1):
    k = random.randint(1, len(digits)-1)
    selected_digits.append(digits[k])
  print(selected_digits)

  selected_chars = selected_digits+selected_lowercase+selected_uppercase+selected_special_characters
  print(selected_chars)
  s = (random.shuffle(selected_chars))
  print(selected_chars)
  password = ''
  for i in range(0, len(selected_chars)):
    password += selected_chars[i]
  
  print(password)
    
    
    

randomPasswordGenerator(999999)