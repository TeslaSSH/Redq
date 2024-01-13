import telepot
import subprocess
from datetime import datetime, timedelta

# Read the bot token from the file
#with open('bot_token.txt', 'r') as file:
   # bot_token = file.read().strip()

# Initialize the bot with the token
bot = telepot.Bot('6892057864:AAErqK-yT3DVE-AcRGJqZP9Mj6fPzhrP-3M')

def add_user(username, password, days, user_info):
    current_date = datetime.now()
    expiration_date = current_date + timedelta(days=int(days))
    expiration_date_str = expiration_date.strftime('%Y-%m-%d')

    # Check if the user already exists
    existing_users = subprocess.check_output(['cat', '/etc/passwd']).decode('utf-8')
    if f'{username}:' in existing_users and user_info.lower() not in existing_users.lower():
        return f"User {username} already exists with a different info."

    # Generate hashed password
    osl_version = subprocess.check_output(['openssl', 'version']).decode('utf-8')
    osl_version = osl_version.split()[1][:5]
    password_option = '-6' if osl_version == '1.1.1' else '-1'
    hashed_password = subprocess.check_output(['openssl', 'passwd', password_option, password]).decode('utf-8').strip()

    # Create user
    try:
        subprocess.run(['sudo', 'useradd', '-M', '-s', '/bin/false', '-e', expiration_date_str, '-K', f'PASS_MAX_DAYS={days}', '-p', hashed_password, '-c', user_info, username], check=True)
        return f"User {username} added successfully!"
    except subprocess.CalledProcessError as e:
        return f"Failed to add user {username}. Error: {e}"

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        command = msg['text']

        if command.startswith('/add'):
            try:
                _, username, password, days, user_info = command.split()
                response = add_user(username, password, days, user_info)
                bot.sendMessage(chat_id, response)
            except ValueError:
                bot.sendMessage(chat_id, "Invalid command format. Use /add username password days user_info")

# Set the command handler
bot.message_loop(handle)

# Keep the program running
while True:
    pass
