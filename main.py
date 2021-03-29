import discord
import os
from correction import fun

#Bot Token
token = 'Insert token here'

#About
about = discord.Embed()
about.title = 'Grammar Nazi'
about.description = 'Bot by @desmofede42'
about.add_field(name='Repository di GitHub', value='[Click Here](https://www.github.com/fliuzzi02/Grammar-Nazi-Bot)', inline=False

#Help
helpCom = discord.Embed()
helpCom.title = "Available commands"
helpCom.description = "Bot's invocation symbol is ``g!``"
helpEmbed.add_field(name='Help', value='``g!help``', inline=False)
helpEmbed.add_field(name='Start monitoring', value='``g!start`', inline=False)
helpEmbed.add_field(name='Stop monitoring', value='``g!stop`', inline=False)
helpEmbed.add_field(name='Available languages', value='``g!lang en/it``', inline=False)

#Client Variables
client = discord.Client()
client.running = False
client.language = 'it'

#On successful login
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#Bot Commands
bot = commands.Bot(command_prefix='g!')

@bot.command(name='about')
async def about(ctx):
    await message.channel.send(embed=about)

@bot.command(name='help')
async def help(ctx):
    await message.channel.send(embed=helpCom)

@bot.command(name='start')
async def start(ctx):
    client.running = True

@bot.command(name='stop')
async def stop(ctx):
    client.running = False

@bot.command(name='lang')
async def lang(ctx, arg):
    if arg == 'it':
        client.language = 'it'
    elif arg == 'en':
        client.language = 'en'
    else:
        await message.channel.send("Selected language not supported")

#When messages are sent
@client.event
async def on_message(message):

    #If the bot itself sent the message
    if message.author == client.user:
        return

    #g!start Message
    if message.content.startswith('g!start') and not client.running:
        client.running = True
        await message.channel.send("Ora sono attivo, mio signore...")

    #g!stop Message
    elif message.content.startswith('g!stop') and client.running:
        client.running = False
        await message.channel.send("Come più gradisce, mio signore...")
    
    #g!lang Message
    elif message.content.startswith('g!lang')

    #Regular message
    elif message.content.startswith('') and client.running:
        misspelled = fun(message.content, client.language)
        if len(misspelled) != 0:
            await message.channel.send(message.author.mention+', hai sbagliato '+str(len(misspelled))+' parole, sei peggio del mio creatore...')


client.run(token)