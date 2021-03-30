import discord
from discord.ext import commands
import os
from correction import fun

#Bot Token
token = 'token here'

#About
about1 = discord.Embed()
about1.title = 'Grammar Nazi'
about1.description = 'Bot by @desmofede42'
about1.add_field(name='GitHub Repository', value='[Click Here](https://www.github.com/fliuzzi02/Grammar-Nazi-Bot)', inline=False)

#Help
helpEmbed = discord.Embed()
helpEmbed.title = "Available commands"
helpEmbed.description = "Bot's invocation symbol is ``g!``"
helpEmbed.add_field(name='Commands list', value='``g!commands``', inline=False)
helpEmbed.add_field(name='Start monitoring', value='``g!start`', inline=False)
helpEmbed.add_field(name='Stop monitoring', value='``g!stop`', inline=False)
helpEmbed.add_field(name='Available languages', value='``g!lang en/it``', inline=False)

#Bot Commands
bot = commands.Bot(command_prefix='g!')
bot.running = False
bot.language = 'en'

@bot.command()
async def about(ctx):
    await ctx.channel.send(embed=about1)

@bot.command(name = "commands")
async def funky_name(ctx):
    await ctx.channel.send(embed=helpEmbed)

@bot.command()
async def start(ctx):
    bot.running = True
    await ctx.channel.send("The bot will start, sir...")

@bot.command()
async def stop(ctx):
    bot.running = False
    await ctx.channel.send("The bot will stop, sir...")

@bot.command()
async def lang(ctx, arg):
    if arg == 'it':
        bot.language = 'it'
        await ctx.channel.send("Language set to Italian")
    elif arg == 'en':
        bot.language = 'en'
        await ctx.channel.send("Language set to English")
    else:
        await ctx.channel.send("Selected language not supported")

#When messages are sent
@bot.event
async def on_message(message):

    #If the bot itself sent the message
    if message.author == bot.user:
        return
    
    #processes commands
    elif message.content.startswith('g!'):
        await bot.process_commands(message)

    #Regular message
    elif bot.running:
        misspelled = fun(message.content, bot.language)
        if len(misspelled) != 0:
            await message.channel.send(message.author.mention+', you misspelled '+str(len(misspelled))+' words, you suck!')

#client.run(token)
bot.run(token)
