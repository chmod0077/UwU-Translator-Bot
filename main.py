import discord
import text_translator as tt
from datetime import datetime

client = discord.Client()
prefix = "^^"

@client.event
async def on_ready():
  print(tt.text_translation("I have logged in as"), "{0.user}".format(client))

@client.event
async def on_message(message):
  if message.author != client.user:
    #prints out every message
    print("\n%s:\nServer: %s\nChannel: #%s\nUser: %s\nContent: %s" %(datetime.now().strftime("%H:%M:%S"), message.guild.name, message.channel.name, message.author.name,
           message.content))

    # detects if there any uwu or owo in the message
    if any(elt in message.content for elt in tt.list_permutations("uwu")) or any(elt in message.content for elt in tt.list_permutations("owo")):
      translation = tt.text_translation(message.content)
      print("\tSent translation: %s" %(translation))
      await message.channel.send(translation)

    # says and translates a given message
    elif message.content.startswith(prefix + "say"):
      translation = tt.text_translation(message.content[len(prefix)+3:])
      print("\tIdentified %ssay command" %prefix)
      print("\tDeleted message from %s" %message.author.name)
      await message.delete()
      print("\tSent translation: %s" %(translation))
      await message.channel.send(translation)



client.run()