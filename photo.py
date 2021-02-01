import telepot
from picamera import PiCamera
import time
from time import sleep
import datetime
from telepot.loop import MessageLoop
from subprocess import call 

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 25

def handle(msg):
    global telegramText
    global chat_id
  
    chat_id = msg['chat']['id']
    telegramText = msg['text']
  
    print('Message received from ' + str(chat_id))
  
    if telegramText == '/start':
        bot.sendMessage(chat_id, 'Security camera is activated.')
	if telegramText == '/photo':
        bot.sendMessage(chat_id, 'photo capturing...')
        filename = "./photo_" + (time.strftime("%y%b%d_%H%M%S"))
        camera.capture(filename + ".jpg")
        bot.sendPhoto(chat_id, photo = open(filename + '.jpg', 'rb'))
        bot.sendMessage(chat_id, 'photo captured!')

bot = telepot.Bot('1501929041:AAEWERk7pzqoxXYd9VJCPkHmbYMYHHScrl4')

MessageLoop(bot,handle).run_as_thread()      
while 1:
    time.sleep(10) 
