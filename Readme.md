# Tesla SSH Bot
---
<p align="center"><img src="https://raw.githubusercontent.com/TeslaSSH/Redq/main/Dupes/20240117_010429.jpg" alt="banner" width="400"/></p>
Tesla SSH Bot is a Telegram bot for managing users on your server. It allows you perform tedious tasks on your server with ease.

---

## Prerequisites

- Ubuntu 22.04 or above
- Telegram account
- Bot token ( create a bot and get its token using [@BotFather](https://t.me/BotFather) )
- Secret key for bot verification (You get it from your server after installing the Bot on it)
- YOU MUST HAVE INSTALLED ANY UDP SCRIPT TO INSTALL THIS BOT, Otherwise, the bot will attempt to first install Tesla SSH UDP Binary on your system.

## Installation
---
1. Go to your telegram account and create a new bot from BotFather. Follow what he tells you to do and when you succeed with the process, he will give you the bot API Token. Copy it and save somewhere for the next step. 

2. Connect to your server using SSH. You can use Termius, Juice SSH or PUTTY if you are not a mobile user.

3. Make sure have root permissions on the server (Recommended)

4. Run the installation script:

<p align="center">
  <img src="https://user-images.githubusercontent.com/76937659/153705486-44e6c1b2-74fa-4d44-be1c-36c8fdb83331.gif"/>
</p>

```  
rm -f ShellBot.sh; wget -O ShellBot.sh https://raw.githubusercontent.com/TeslaSSH/Redq/main/ShellBot.sh && chmod 777 ShellBot.sh && ./ShellBot.sh
```   

<p align="center">
  <img src="https://user-images.githubusercontent.com/76937659/153705486-44e6c1b2-74fa-4d44-be1c-36c8fdb83331.gif"/>
</p>

- Chooose an option that says "install Bot" and then follow the prompts


5. Now when done, go back to Telegram and open a chat with the bot you just created and start adding, removing and renewing users among others without leaving Telegram.
   
## Usage

- Just use the bot Buttons to interract directly with your server.
- Regardless of whether you reboot the server or not, the bot will just persistently run unless stopped by you via the bot menu.
- To Access Bot Manager Menu on the server side, just type `bot` into the terminal
  
## BOT FUNCTIONALITIES
  
  - Adding new users to the UDP Server Remotely without seeing terminal again!
  - Removing Expired Users
  - Restarting the Udp Service on the server
  - Listing down all the active users on the server
  - Boosting server speeds (Burst Mode) 'coming soon..'
 
  All these can be done through the bot, without leaving telegram!


## What's New? 
- Bot secret key varification removed. Will be back in the next versions
- Bot can now run automatically after server reboot.
- System RAM consumption rate reduced by about 49.6%
- Faster Bot response times
- No need to first connect to a different server in order to communicate with the server. The Bot does it crazily🤠
- Can reboot Your server wirelessly. No need to use PUTTY, JUICE SSH, Termux or Termius. The Bot does it quickly.


## Issues

If you encounter any issues or have suggestions, please [open an issue](https://github.com/TeslaSSH/Redq/issues).

## Developers
- [Tesla SSH](https://t.me/teslassh) - Bot Developer

- [Ted Hackwell](https://t.me/hackwell101) - Bot Logic Organizer. 

### Contributers
- Nicholas Owor (UG) -encrypted it. 

## JOIN OUR UDP COMMUNITY

 [UDP CUSTOM](t.me/udpcustom).

You have an idea to add? You can be a contributer!

## **Usage Policy Notice**

You can download and share the bot as long as you credit us, don't modify the code, and don't use it for commercial purposes without our permission.
To provide clarity on these terms, we are considering the use of the Creative Commons Attribution-NonCommercial-NoDerivatives (CC BY-NC-ND) license.
