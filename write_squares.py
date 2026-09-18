def write_squares(num):
  a = list(range(0, num+1, 1))
  b = list(map(lambda x: x * x, a))
  for i in range(0, len(b)):
    print('{} ^ 2 = {}'.format(i, b[i]))
  

write_squares(100)