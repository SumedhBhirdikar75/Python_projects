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