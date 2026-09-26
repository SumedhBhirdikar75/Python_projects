def create_list():
  leng = int(input('Enter length of the list'))
  res_list = []
  for i in range(leng):
    app = int(input('Enter character {}'.format(i+1)))
    res_list.append(app)
  print(res_list)

  search_initiate = int(input('which character to search for? '))
  index = []
  for i in range(0, len(res_list)):
    if res_list[i] == search_initiate:
      index.append(i)

  if len(index) == 1:
    print('{} is at index {}'.format(search_initiate, index))

  elif len(index) == 0:
    print(f'Couldnt find {search_initiate}')

  else:    
    print('{} is at indices {}'.format(search_initiate, index))
      
      
  

create_list()


# ##### version 2: takes in multiple data type inputs, allows you to search even if you forget the data type


def create_list():
  leng = int(input('Enter length of the list'))
  res_list = []
  raw_res_list = []
  for i in range(leng):
    app = input('Enter character {} with its data type. eg int-1 or str-abc'.format(i+1))
    data_type = app.split('-',1)[0]
    print(data_type)
    if data_type.lower() == 'int':
      res_list.append(int(app.split('-',1)[1]))


    if data_type.lower() == 'str':
      res_list.append(app.split('-',1)[1])

    if data_type.lower() == 'float':
      res_list.append(float(app.split('-',1)[1]))
    
    
    raw_res_list.append(app)

    print(res_list)
    print(raw_res_list)

  search_initiate = input('Do you know the data type of the characrter you want to search(y/n)? ')
  if search_initiate.lower() == 'y':
    search = input('Enter the char you want to search with its type (eg. int-1 or str-abc) ')
    search_char_data_type = search.split('-',1)[0]
    if search_char_data_type.lower() == 'int':
      search_character = int(search.split('-',1)[1])

    if search_char_data_type.lower() == 'str':
      search_character = (search.split('-',1)[1])

    if search_char_data_type.lower() == 'float':
      search_character = float(search.split('-',1)[1])

    index = []
    for i in range(0, len(res_list)):
      if res_list[i] == search_character:
        index.append(i)

    if len(index) == 1:
      print('{} is at index {}'.format(search_character, index))

    elif len(index) == 0:
      print(f'Couldnt find {search_character}')

    else:
      print('{} is at indices {}'.format(search_character, index))

  if search_initiate.lower() == 'n':
    print('We will try to find it by using your previous inputs')
    search_char = input('search for the character. No dtype needed ')
    index = []
    dtype = []
    for i in range(len(raw_res_list)):
      if raw_res_list[i].split('-', 1)[1].lower() == search_char.lower():
        #print(raw_res_list[i].split('-')[1].lower())
        index.append(i)
        dtype.append(raw_res_list[i].split('-',1)[0])
    if len(index) == 1:
     print('{} is at index {}'.format(search_char, index))

    elif len(index) == 0:
      print(f'Couldnt find {search_char}')

    else:
      print('{} is at indices {}. There dtypes are {} '.format(search_char, index,dtype ))


    



create_list()
