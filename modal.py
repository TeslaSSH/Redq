import telepot
import subprocess

# Read the bot token from the file
#with open('bot_token.txt', 'r') as file:
   # bot_token = file.read().strip()

# Initialize the bot with the token
bot = telepot.Bot('6892057864:AAErqK-yT3DVE-AcRGJqZP9Mj6fPzhrP-3M')

def add_user(nameuser, userpass, userdays, limiteuser):
    fecha = subprocess.check_output(['date', '+%d-%m-%y-%R']).decode().strip()
    check_user_command = f"cat /etc/passwd | grep {nameuser}: | grep -vi [a-z]{nameuser} | grep -v [0-9]{nameuser} >/dev/null"
    
    # Check if the user already exists
    if subprocess.call(check_user_command, shell=True) == 0:
        return 1
    
    valid = subprocess.check_output(['date', '+%C%y-%m-%d', '-d', f'+{userdays} days']).decode().strip()
    osl_v = subprocess.check_output(['openssl', 'version']).decode().split()[1][:5]

    if osl_v == '1.1.1':
        pass_hash = subprocess.check_output(['openssl', 'passwd', '-6', userpass]).decode().strip()
    else:
        pass_hash = subprocess.check_output(['openssl', 'passwd', '-1', userpass]).decode().strip()

    useradd_command = [
        'useradd',
        '-M',
        '-s', '/bin/false',
        '-e', valid,
        '-K', f'PASS_MAX_DAYS={userdays}',
        '-p', pass_hash,
        '-c', f'{limiteuser},{userpass}',
        nameuser
    ]
    
    subprocess.run(useradd_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    return subprocess.CompletedProcess.returncode

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
            help_message = "Usage guide:\n/add - Add a new user interactively"
            bot.sendMessage(chat_id, help_message)

        elif command == '/add':
            bot.sendMessage(chat_id, "Enter username:")
            nameuser = get_user_input(chat_id)
            bot.sendMessage(chat_id, "Enter password:")
            userpass = get_user_input(chat_id)
            bot.sendMessage(chat_id, "Enter number of days:")
            userdays = int(get_user_input(chat_id))
            bot.sendMessage(chat_id, "Enter user limit:")
            limiteuser = get_user_input(chat_id)

            result = add_user(nameuser, userpass, userdays, limiteuser)
            
            if result == 0:
                success_message = f"User {nameuser} added successfully!"
                bot.sendMessage(chat_id, success_message)
            else:
                error_message = f"Failed to add user {nameuser}."
                bot.sendMessage(chat_id, error_message)

def get_user_input(chat_id):
    while True:
        updates = bot.getUpdates()
        if updates:
            last_update = updates[-1]['message']
            if 'text' in last_update:
                return last_update['text']

# Set the command handler
bot.message_loop(handle)

# Keep the program running
while True:
    pass
