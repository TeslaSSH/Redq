import telepot
import subprocess

# Read the bot token from the file
#with open('bot_token.txt', 'r') as file:
   # bot_token = file.read().strip()

# Initialize the bot with the token
bot = telepot.Bot('6892057864:AAErqK-yT3DVE-AcRGJqZP9Mj6fPzhrP-3M')

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        command = msg['text']

        if command == '/start':
            welcome_message = ("Hello, welcome to Tesla SSH scripts manager. "
                               "You can use me to create more users for your server!\n"
                               "Press /start to reload the bot\n"
                               "Press /help to see the usage guide\n"
                               "Press /add to add user")
            bot.sendMessage(chat_id, welcome_message)

        elif command == '/help':
            help_message = "Usage guide:\n/add [username] - Add a new user"
            bot.sendMessage(chat_id, help_message)

        elif command.startswith('/add'):
            username = command.split()[1]
            subprocess.call(['sudo', 'adduser', username])
            success_message = f"User {username} added successfully!"
            bot.sendMessage(chat_id, success_message)

# Set the command handler
bot.message_loop(handle)

# Keep the program running
while True:
    pass
