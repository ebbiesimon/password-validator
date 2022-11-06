import re
user_password = ''
while True:
  user_password = input('input your password ')
  if len(user_password) < 9 or len(user_password) > 12:
    print('password lenght should be between 9 and 12')
  elif re.search('[0-9]',user_password) == None :
    print('password must contain atleast 3 numbers')
  elif re.search('[a-z]', user_password) == None:
    print('password must contain atleast 5 alphabet')
  elif re.search(r'[&#$!?"()]',user_password) == None:
    print('password must contain atleast 3 special characters')
  else:
    print('you have successfully created your password')
    break