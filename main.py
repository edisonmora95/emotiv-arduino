import keyboard  #Using module keyboard
import serial    #Conecting with Arduino

PORT    = 'COM6'
arduino = serial.Serial(PORT, 9600)

#Beginning of the loop, waiting for keypressed event
while True:
  try: #used try so that if user pressed other than the given keys error will not be shown
    if keyboard.is_pressed('w'):
      print('Forward')
      arduino.write(b'9')
    if keyboard.is_pressed('d'):
      print('Right')
      arduino.write(b'8')
    if keyboard.is_pressed('a'):
      print('Left')
      arduino.write(b'7')
    if keyboard.is_pressed('s'):
      print('Back')
      arduino.write(b'6')
    if keyboard.is_pressed('q'):
      print('Closing program')
      arduino.write(b'5')
      break
    else:
      pass
  except:
    pass