import telepot
import subprocess
from datetime import datetime, timedelta
import time
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
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
    passs = subprocess.check_output(['openssl', 'passwd', password_option, password]).decode('utf-8').strip()

    # Create user
    try:
        subprocess.run(['sudo', 'useradd', '-M', '-s', '/bin/false', '-e', expiration_date_str, '-K', f'PASS_MAX_DAYS={days}', '-p', passs, '-c', f'{user_info},{password}', username], check=True)
        return f"User {username} added successfully!"
    except subprocess.CalledProcessError as e:
        return f"Failed to add user {username}. Error: {e}"

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    # Define custom keyboard buttons with smaller size in a single row
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='Restart', resize_keyboard=True),
         KeyboardButton(text='Add User', resize_keyboard=True),
         KeyboardButton(text='Help', resize_keyboard=True)],
    ], resize_keyboard=True)

    if content_type == 'text':
        command = msg['text']

        if command.lower() == 'restart':
            start_message = ("🔰 WELCOME TO TESLA SSH BOT 🔰. \n"
                             "━━━━━━━━━━━━━━━━━━━━━━━━━ \n"
                             "\n"
                             "You can use me to add users to your server!\n"
                             "\n"
                             "To reload the bot, Press /start\n"
                             "To see the usage guide, Press /help\n"
                             "To add user, Press /add \n"
                             "\n"
                             "🔰 Made with spirit. \n"
                             "========================= \n"
                             "By: @TESLASSH \n"
                             "Mastered by: @hackwell101 \n"
                             "Join @udpcustom")

            # Send the start message with the custom keyboard
            bot.sendMessage(chat_id, start_message, reply_markup=keyboard)

        elif command.lower() == 'help':
            help_message = ("HOW TO USE BOT:\n"
                            "━━━━━━━━━━━━━━━━━━━━━━━━━"
                            "\n"
                            "- To Add a new user, \n"
                            "Send /add [username] [password] [days]\n"
                            "\n"
                            "Example:\n" "/add Nicolas passwad 30\n"
                            "\n"
                            "if you are facing issues with the bot,\n"
                            "press /start\n"
                            "\n"
                            "Contact: @teslassh"
                            )
            bot.sendMessage(chat_id, help_message, reply_markup=keyboard)

        elif command.lower() == 'add user':
            bot.sendMessage(chat_id, "To add a user, use the format: /add [username] [password] [days]", reply_markup=keyboard)

        elif command.startswith('/add'):
            try:
                _, username, password, days = command.split()
                # Introduce a sleep of 3 seconds
                time.sleep(3)
                response = add_user(username, password, days, user_info="bot")
                bot.sendMessage(chat_id, response, reply_markup=keyboard)
            except ValueError:
                bot.sendMessage(chat_id, "Invalid command format. Use /add [username] [password] [days]", reply_markup=keyboard)

# Set the command handler
bot.message_loop(handle)

# Keep the program running
while True:
    pass
