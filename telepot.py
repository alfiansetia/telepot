import sys
import time
import random
import datetime
import telepot

def handle(msg):
	chat_id = msg['chat']['id']
	command = msg['text']

	print 'Got command: %s' % command

	if command == '/roll':
		bot.sendMessage(chat_id, random.randint(1,6))
	elif command == '/time':
		bot.sendMessage(chat_id, str(datetime.datetime.now()))
bot = telepot.Bot('1135612638:AAGh3d4sakQq945i_PWPUxlCLC4QdGL3lSM')
bot.message_loop(handle)
print 'I am Listening'

while 1 :
	time.sleep(10)