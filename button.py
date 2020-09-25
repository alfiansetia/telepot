import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import sys
import telepot
import time

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

while True: # Run forever
    text = 'TESSSSSSSSS'
    chat_id = 635000156
    bot = telepot.Bot('1135612638:AAGh3d4sakQq945i_PWPUxlCLC4QdGL3lSM')
    if GPIO.input(10) != GPIO.LOW:
        bot.sendMessage(chat_id, text)
        print("Button was pushed!")
    else:
        print("Im stanby")





#print('SUKSES')