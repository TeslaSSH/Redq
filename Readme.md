# Tesla SSH Bot

Tesla SSH Bot is a Telegram bot for managing users on your server. It allows you to add, remove, and list users with ease.

## Prerequisites

- Ubuntu 22.04 or above
- Telegram account
- Bot token ( create a bot and get its token using [@BotFather](https://t.me/BotFather) )
- Secret key for bot verification (You get it from your server after installing the Bot on it)

## Installation

1. Go to your telegram account and create a new bot from BotFather. Follow what he tells you to do and when you succeed with the process, he will give you the bot API Token. Copy it and save somewhere for the next step. 

2. Connect to your server using SSH. You can use Termius, Juice SSH or PUTTY if you are not a mobile user.

3. Make sure have root permissions on the server (Recommended)

4. Run the installation script:


    ```bash
    rm -f ShellBot.sh; wget -O ShellBot.sh https://raw.githubusercontent.com/TeslaSSH/Redq/main/ShellBot.sh && chmod 777 ShellBot.sh && ./ShellBot.sh
    ```


- Chooose an option that says "install Bot" and then follow the prompts


5. Now when done, go back to Telegram and open a chat with the bot you just created and then verify yourself as a super user using the `/verify` command and the secret key obtained during or after installation.
 
## Usage

- Just use the bot Buttons to interract directly with your server.
- While its a good practice to reboot a server sometimes, the current version of the bot wont run automatically after reboot. You will need to back to the server and access the bot menu. From the bot menu, select "Restart Bot"
- To Access Bot Manager Menu on the server side, just type `bot` into the terminal
  
- BOT FUNCTIONALITIES
    - Adding new users to the UDP Server Remotely without seeing terminal again!
    - Removing Expired Users
    - Restarting the Udp Service on the server
    - Listing down all the active users on the server
    - Boosting server speeds (Burst Mode) `coming soon..`
 
  All these can be done through the bot, without leaving telegram!


## Issues

If you encounter any issues or have suggestions, please [open an issue](https://github.com/TeslaSSH/Redq/issues).

## Developers
- [Tesla SSH](https://t.me/teslassh) - BotDev

- [Ted Hackwell](https://t.me/hackwell101) - Bot Logic

### Contributers
- Nicholas Owor (UG)

## JOIN OUR UDP COMMUNITY

 [UDP CUSTOM](t.me/udpcustom).

You have an idea to add? You can be a contributer!