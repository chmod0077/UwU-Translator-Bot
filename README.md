# UwU-Translator-Bot
### A Discord Bot that translates any sentence into its UwU and OwO form.
![pfp](/medias/uwu_translator_bot.png)

## Commands
### Prefix: ^^
- ^^whoru: Short description of myself
- ^^commands: See authorized commands
- your_message containing uwu/owo: Reply to your_message now transformed into its UwU and OwO form
- ^^say + your_message: Translation of your message into its UwU and OwO form
- ^^gif: Send a random a gif that is very much UwU
- ^^cpasta: Send a random a copypasta that is very much OwO

## How it works
### This bot was coded in Python using the discord.py module.
media_retriever.py (mr) and text_translator.py (tt) are both modules for main.py.\
main.py is the client file for the discord bot and analyzes each incoming message\
and if it detects certain words, it calls functions from mr and tt in order to execute\
any requested message.
