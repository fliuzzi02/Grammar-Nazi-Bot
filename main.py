import discord
from discord.ext import commands
import os
from correction import fun

#Bot Token
token = 'Insert token here'

#About
about1 = discord.Embed()
about1.title = 'Grammar Nazi'
about1.description = 'Bot by @desmofede42'
about1.add_field(name='Repository di GitHub', value='[Click Here](https://www.github.com/fliuzzi02/Grammar-Nazi-Bot)', inline=False)

#Help
helpEmbed = discord.Embed()
helpEmbed.title = "Available commands"
helpEmbed.description = "Bot's invocation symbol is ``g!``"
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
    await ctx.send(embed=about1)

@bot.command(name='helpme')
async def helpme(ctx):
    await ctx.send(embed=helpEmbed)

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
        await ctx.send("Selected language not supported")

#When messages are sent
@client.event
async def on_message(message):

    #If the bot itself sent the message
    if message.author == client.user:
        return

    #Regular message
    elif not message.content.startswith('g!') and client.running:
        misspelled = fun(message.content, client.language)
        if len(misspelled) != 0:
            await message.channel.send(message.author.mention+', hai sbagliato '+str(len(misspelled))+' parole, sei peggio del mio creatore...')


client.run(token)