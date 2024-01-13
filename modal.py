import telepot
import subprocess

# Replace 'YOUR_BOT_TOKEN' with your Telegram bot token
bot = telepot.Bot('6892057864:AAErqK-yT3DVE-AcRGJqZP9Mj6fPzhrP-3M')

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        command = msg['text']
        if command.startswith('/adduser'):
            username = command.split()[1]
            subprocess.call(['sudo', 'adduser', username])

# Set the command handler
bot.message_loop(handle)

# Keep the program running
while True:
    pass
