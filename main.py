# i've made everything here so please don't accuse me of stealing code
# though it's pretty shitty so idk why you would do that lol

import discord
from datetime import datetime
from text_translator import TextTranslator
from media_retriever import MediaRetriever
import os
import json
from pathlib import Path


bot_prefix = "^^"
client = discord.Client(status=discord.Status.idle,
                        activity=discord.Activity(name=("%scommands" % bot_prefix), type=discord.ActivityType.watching))
start_time = datetime.now()

current_dir = str(Path(__file__).parent.resolve()) + '/medias/'
TT = TextTranslator(current_dir)
MR = MediaRetriever(current_dir)


def get_tokens():
    current_working_file = str(Path(__file__).parent.resolve())
    if os.path.exists(current_working_file + "/config.json"):
        with open(current_working_file + "/config.json") as file:
            config_data = json.load(file)
    else:
        config_template = {"discord_token": "", "api_key": ""}
        with open(current_working_file + "/config.json", "w+") as file:
            json.dump(config_template, file)

    return config_data["discord_token"], config_data["api_key"]


@client.event
async def on_ready():
    print(
        TT.text_translation("I have logged in as"),
        "{0.user}".format(client))

    active_servers = client.guilds
    print("Active in %s servers" % len(active_servers))
    active_servers_list = sorted([guild.name for guild in active_servers])
    print(active_servers_list)


@client.event
async def on_message(message):
    if message.author != client.user:
        # prints out every message
        # print(
        # "%s (%s, %s, %s, %s)" %
        # (datetime.now().strftime("%H:%M:%S"),
        # message.guild.name,
        # message.channel.name,
        # message.author.name,
        # message.content))

        # useful commands
        # says and translates a given message
        if message.content.startswith(bot_prefix + "say"):
            translation = TT.text_translation(
                message.content[len(bot_prefix) + 4:])
            print("%s: Identified %ssay command" %
                  (datetime.now().strftime("%H:%M:%S"), bot_prefix))
            print("\tDeleted message from %s" % message.author.name)
            await message.delete()
            print("\tSent translation: %s" % (translation))
            await message.channel.send(translation)

        elif message.content.startswith(bot_prefix + "gif"):
            gif_url = MR.retrieve_gif("owo", 20, api_key)
            print("%s: Identified %sgif command" %
                  (datetime.now().strftime("%H:%M:%S"), bot_prefix))
            print("\tSent gif: %s" % (gif_url))
            await message.channel.send(gif_url)

        elif message.content.startswith(bot_prefix + "cpasta"):
            copypasta_translation = TT.text_translation(
                MR.retrieve_copypasta("copypastas.txt"))
            print("%s: Identified %scpasta commands" %
                  (datetime.now().strftime("%H:%M:%S"), bot_prefix))
            print("\tSent copypasta: %s" % (copypasta_translation))
            await message.channel.send(copypasta_translation)

        # hidden commands
        elif message.content.startswith(bot_prefix + "stats"):
            uptime = datetime.now() - start_time
            print("%s: Identified %sstats command" %
                  (datetime.now().strftime("%H:%M:%S"), bot_prefix))
            print("\tDeleted message from %s" % message.author.name)
            await message.delete()
            print("\tUptime: %s\n\tServers: %s" %
                  (uptime, str(len(client.guilds))))
            await message.channel.send("Uptime: %s\nServers: %s" % (uptime, str(len(client.guilds))))

        elif message.content.startswith(bot_prefix + "read"):
            print("%s: Identified %sread command" %
                  (datetime.now().strftime("%H:%M:%S"), bot_prefix))
            print("\tDeleted message from %s" % message.author.name)
            await message.delete()
            try:
                reading = MR.retrieve_text(
                    message.content[len(bot_prefix) + 5:])
                print("\tSent %s" % message.content[len(bot_prefix) + 5:])
                await message.channel.send(TT.text_translation(reading))
            except BaseException:
                print("\tCould not send %s" %
                      message.content[len(bot_prefix) + 5:])

        # useless commands
        elif message.content.startswith(bot_prefix + "whoru"):
            print("%s: Identified %swhoru command" %
                  (datetime.now().strftime("%H:%M:%S"), bot_prefix))
            await message.channel.send(TT.text_translation("Hello! My name is ") + "{0.user}\nMy pronouns are (NVIDIA GeForce RTX 2060 Intel Core i5-10400F CPU 16.0GB RAM/ them).\nMy main purpose is to translate your text into something very UwU.\nI have been created by Thomas Frs in only one day! Which probably explains why my organism\nis a complete mess and I can't do much :( (and im very cringe)".format(client))

        elif message.content.startswith(bot_prefix + "commands"):
            print("%s: Identified %scommands command" %
                  (datetime.now().strftime("%H:%M:%S"), bot_prefix))
            await message.channel.send("*Prefix:* ``%s``\n*Commands:*\n``%swhoru``: I talk extensively about myself because I don't have a gf\n``%scommands``: I display this message once again, because why not\n``your_message containing uwu/owo``: I reply to your message and translate it into its UwU and OwO form\n``%ssay + your_message``: I delete your message and translate it into its UwU and OwO form\n``%sgif``: I post a random gif that is very much OwO\n``%scpasta``: I post a random copypasta that is very much OwO" % (bot_prefix, bot_prefix, bot_prefix, bot_prefix, bot_prefix, bot_prefix))  # bot_prefix

        # detects if there any uwu or owo in the message
        elif any(elt in message.content for elt in TT.list_permutations("uwu")) or any(
                elt in message.content for elt in TT.list_permutations("owo")):
            translation = TT.text_translation(message.content)
            print("%s: Identified uwu/owo in content" %
                  (datetime.now().strftime("%H:%M:%S")))
            print("\tSent translation: %s" % (translation))
            await message.channel.send(translation)


discord_token, api_key = get_tokens()
client.run(discord_token)
