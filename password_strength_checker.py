a = input('enter password')
num = [1,2,3,4,5,6,7,8,9,0]
nums_in_a = []
password_str = ''
has_numbers = ''
has_letters = ''
is_long = ''

if len(a) >= 8:
    is_long = 'Check'

for i in a:
  for k in num:
    try:
      if int(i) == k:
        nums_in_a.append(int(i))
    
    except:
      continue

  if len(nums_in_a) > 0:
    has_numbers = 'Check'
      
lets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lets_in_a = []

for i in a:
  for l in lets:
    try:
      if i.lower() == l:
        lets_in_a.append(i.lower())
      
    
    except:
      continue

if len(lets_in_a) > 0:
    has_letters = 'Check'

print(
  has_letters, has_numbers, is_long
)



if has_numbers and has_letters and is_long == 'Check':
    password_str = 'strong'
    
elif has_numbers== '' and has_letters == 'Check' and is_long == 'Check' :
    password_str = 'medium'

elif has_numbers== 'Check' and has_letters == '' and is_long == 'Check' :
    password_str = 'medium'

elif has_numbers== 'Check' and has_letters == 'Check' and is_long == '' :
    password_str = 'medium'

if has_numbers and has_letters and is_long != 'Check':
    password_str = 'weak'

print(password_str)
      
    
      