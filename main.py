import discord
import os
from correction import fun

#Bot Token
token = 'Insert token here'

#About
about = discord.Embed()
about.title = 'Grammar Nazi'
about.description = 'Bot by @desmofede42'

#Help
helpCom = discord.Embed()
helpCom.title = "Available commands"
helpCom.description = "Bot's invocation symbol is ``g!``"


#Client Variables
client = discord.Client()
client.running = False

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('g!start') and not client.running:
        client.running = True
        await message.channel.send("Ora sono attivo, mio signore...")

    elif message.content.startswith('g!stop') and client.running:
        client.running = False
        await message.channel.send("Come più gradisce, mio signore...")
        
    elif message.content.startswith('') and client.running:
        misspelled = fun(message.content)
        if len(misspelled) != 0:
            await message.channel.send(message.author.mention+', hai sbagliato '+str(len(misspelled))+' parole, sei peggio del mio creatore...')


client.run(token)
