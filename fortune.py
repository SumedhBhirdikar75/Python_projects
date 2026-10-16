def fortune_generator():
  import random
  fortune_lst = ['A great day ahead', 'Might regret your past decision', 'A very productive day ahead', 'Might be the worst day yet', 'Mediocre', 'awesome', 'Amazing']
  selector = random.randint(0, len(fortune_lst) -1)
  #print(selector)
  for i in fortune_lst:
    fortune = (fortune_lst[selector])
  print(fortune)
  print('This is just a prediction. completely random. Your future lies in your own hands.')



fortune_generator()
