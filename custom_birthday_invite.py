def write_custom_invite(lst_of_members, venue, time):
  for i in range(0, len(lst_of_members)):
    print(f'Dear {lst_of_members[i]},you are invited to my birthday party. Please come to {venue} at {time}. See you there\nRegards,\nSumedh')


write_custom_invite(['a', 'b', 'c'], 'abc cafe', '5 pm')