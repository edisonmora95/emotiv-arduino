import keyboard  # Using module keyboard
import serial    # Conecting with Arduino

PORT     = 'COM6'  # Remember to change the port to the one the HC05 is using
arduino  = serial.Serial(PORT, 9600)
last_key = 'q'

# Beginning of the loop, waiting for keypressed event
while True:
  try: # Used try so that if user pressed other than the given keys error will not be shown
    # Check if the user pressed the same key as last time
    if keyboard.is_pressed(last_key):
      pass
    else:
      if keyboard.is_pressed('w'):
        last_key = 'w'
        print('Forward')
        arduino.write(b'9')
      if keyboard.is_pressed('d'):
        last_key = 'd'
        print('Right')
        arduino.write(b'8')
      if keyboard.is_pressed('a'):
        last_key = 'a'
        print('Left')
        arduino.write(b'7')
      if keyboard.is_pressed('s'):
        last_key = 's'
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