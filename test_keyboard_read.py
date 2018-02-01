import keyboard #Using module keyboard

#Beginning of the loop, waiting for keypressed event
while True:
  try: #used try so that if user pressed other than the given key error will not be shown
    if keyboard.is_pressed('k'):#if key 'q' is pressed 
      print('Sending signal to arduino')
    if keyboard.is_pressed('q'):
    	print('Closing program')
    	break
    else:
      pass
  except:
    pass