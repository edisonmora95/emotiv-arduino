import keyboard #Using module keyboard
import serial		#Conecting with Arduino
import time

#arduino = serial.Serial(0) 
#arduino.port('COM5')
arduino = serial.Serial('COM5', 9600)

#Beginning of the loop, waiting for keypressed event
while True:
  try: #used try so that if user pressed other than the given key error will not be shown
    if keyboard.is_pressed('k'):#if key 'q' is pressed 
      print('Sending signal to Arduino')
      arduino.write(b'9')	#Send as byte
    if keyboard.is_pressed('q'):
    	print('Closing program')
    	arduino.close()			#Closing the serial
    	break
    else:
      pass
  except:
    pass