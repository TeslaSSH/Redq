import telepot
import subprocess

# Read the bot token from the file
#with open('bot_token.txt', 'r') as file:
  #  bot_token = file.read().strip()

# Initialize the bot with the token
bot = telepot.Bot('6892057864:AAErqK-yT3DVE-AcRGJqZP9Mj6fPzhrP-3M')

def add_user(nameuser, userpass, userdays, limiteuser):
    fecha = subprocess.check_output(["date", "+%d-%m-%y-%R"]).decode().strip()
    user_exists = subprocess.call(["grep", f"{nameuser}:", "/etc/passwd", "|", "grep", "-vi", f"[a-z]{nameuser}", "|", "grep", "-v", f"[0-9]{nameuser}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if user_exists == 0:
        return "User already exists"

    valid = subprocess.check_output(["date", '+%C%y-%m-%d', '-d', f'+{userdays} days']).decode().strip()
    osl_v = subprocess.check_output(["openssl", "version"]).decode().split()[1][:5]

    if osl_v == '1.1.1':
        pass_hash = subprocess.check_output(["openssl", "passwd", "-6", userpass]).decode().strip()
    else:
        pass_hash = subprocess.check_output(["openssl", "passwd", "-1", userpass]).decode().strip()

    subprocess.call(["useradd", "-M", "-s", "/bin/false", "-e", valid, "-K", f"PASS_MAX_DAYS={userdays}", "-p", pass_hash, "-c", f"{limiteuser},{userpass}", nameuser], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return f"User {nameuser} added successfully!"

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
            help_message = "Usage guide:\n/add - Add a new user"
            bot.sendMessage(chat_id, help_message)

        elif command == '/add':
            bot.sendMessage(chat_id, "Enter username:")
            bot.message_loop(lambda msg_user: handle_add_user(msg_user, chat_id))

def handle_add_user(msg, chat_id):
    content_type, _, _ = telepot.glance(msg)

    if content_type == 'text':
        nameuser = msg['text']
        bot.sendMessage(chat_id, "Enter password:")
        bot.message_loop(lambda msg_pass: handle_password(msg_pass, chat_id, nameuser))

def handle_password(msg, chat_id, nameuser):
    content_type, _, _ = telepot.glance(msg)

    if content_type == 'text':
        userpass = msg['text']
        bot.sendMessage(chat_id, "Enter number of days:")
        bot.message_loop(lambda msg_days: handle_days(msg_days, chat_id, nameuser, userpass))

def handle_days(msg, chat_id, nameuser, userpass):
    content_type, _, _ = telepot.glance(msg)

    if content_type == 'text':
        userdays = msg['text']
        bot.sendMessage(chat_id, "Enter user limit:")
        bot.message_loop(lambda msg_limit: handle_limit(msg_limit, chat_id, nameuser, userpass, userdays))

def handle_limit(msg, chat_id, nameuser, userpass, userdays):
    content_type, _, _ = telepot.glance(msg)

    if content_type == 'text':
        limiteuser = msg['text']
        result = add_user(nameuser, userpass, userdays, limiteuser)
        bot.sendMessage(chat_id, result)

# Set the command handler
bot.message_loop(handle)

# Keep the program running
while True:
    pass
