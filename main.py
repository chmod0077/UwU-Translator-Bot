# i've made everything here so please don't accuse me of stealing code
# though it's pretty shitty so idk why you would do that lol

import discord
from datetime import datetime
import text_translator as tt
import media_retriever as mr
import os

client = discord.Client()
prefix = "^^"


@client.event
async def on_ready():
    print(
        tt.text_translation("I have logged in as"),
        "{0.user}".format(client))


@client.event
async def on_message(message):
    if message.author != client.user:
        # prints out every message
        print(
            "\n%s:\nServer: %s\nChannel: #%s\nUser: %s\nContent: %s" %
            (datetime.now().strftime("%H:%M:%S"),
             message.guild.name,
             message.channel.name,
             message.author.name,
             message.content))

        # detects if there any uwu or owo in the message
        if any(elt in message.content for elt in tt.list_permutations("uwu")) or any(
                elt in message.content for elt in tt.list_permutations("owo")):
            translation = tt.text_translation(message.content)
            print("\tSent translation: %s" % (translation))
            await message.channel.send(translation)

        # says and translates a given message
        elif message.content.startswith(prefix + "say"):
            translation = tt.text_translation(
                message.content[len(prefix) + 3:])
            print("\tIdentified %ssay command" % prefix)
            print("\tDeleted message from %s" % message.author.name)
            await message.delete()
            print("\tSent translation: %s" % (translation))
            await message.channel.send(translation)

        elif message.content.startswith(prefix + "gif"):
            gif_url = mr.retrieve_gif("owo", 20)
            print("\tIdentified %sgif command" % prefix)
            print("\tSent gif: %s" % (gif_url))
            await message.channel.send(gif_url)

        elif message.content.startswith(prefix + "whoru"):
            print("\tIdentified %swhoru command" % prefix)
            await message.channel.send(tt.text_translation("Hello! My name is ") + "{0.user}".format(client))
            await message.channel.send(tt.text_translation("My pronouns are (NVIDIA GeForce RTX 2060 Intel Core i5-10400F CPU 16.0GB RAM/ them)."))
            await message.channel.send(tt.text_translation("My main purpose is to translate your text into its something very UwU."))
            await message.channel.send(tt.text_translation("I have been created by Anne Frs in only one day! Which probably explains why my organism\nis a complete mess and I can't do much :("))

        elif message.content.startswith(prefix + "commands"):
            print("\tIdentified %scommands command" % prefix)
            await message.channel.send("*Prefix:* ``%s``" % prefix)  # prefix
            await message.channel.send("*Commands:*")
            # whoru
            await message.channel.send("\t``%swhoru``: I talk extensively about myself because I don't have a gf" % prefix)
            # commands
            await message.channel.send("\t``%scommands``: I display this message once again, because why not" % prefix)
            # say
            await message.channel.send("\t``%ssay + your_message``: I delete your message and translate it into its UwU and OwO form" % prefix)
            # gif
            await message.channel.send("\t``%sgif``: I post a random gif that is very much OwO" % prefix)
            # gif
            await message.channel.send("\t``(uwu/owo) + your_message``: I delete your message and translate it into its UwU and OwO form")

client.run(os.getenv("discord_token"))
