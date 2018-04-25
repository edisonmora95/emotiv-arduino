## Description
This is a program created in Python that connects the Emotiv to an arduino.
Used to control a car with your thoughts.

## Modules needed
*	pyautogui		( For keypressed test )
*	keyboard		( Reading from keyboard )
*	pyserial		( Arduino connection )

```
pip install pyautogui
pip install keyboard
pip install pyserial	
```

## Program
1. Connect arduino
2. Change port variable to the one the HC05 module is using in main.py
3. Open terminal
4. cd into proyect directory
5. Run main.py
6. Prepare Emotiv
7. Connect the Emotiv to the console running main.py

If you want to test it without the Emotiv, in the console running main.py you can type the following:
```
w -> to move forward
s -> to move backwards
d -> to move to the right
a -> to move to the left
q -> to quit
```
