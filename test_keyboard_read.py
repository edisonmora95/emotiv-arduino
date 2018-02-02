import keyboard #Using module keyboard

#Beginning of the loop, waiting for keypressed event
while True:
  try: #used try so that if user pressed other than the given key error will not be shown
    if keyboard.is_pressed('w'):
      print('Forward')
    if keyboard.is_pressed('d'):
      print('Right')
    if keyboard.is_pressed('a'):
      print('Left')
    if keyboard.is_pressed('s'):
      print('Back')
    if keyboard.is_pressed('q'):
    	print('Closing program')
    	break
    else:
      pass
  except:
    pass