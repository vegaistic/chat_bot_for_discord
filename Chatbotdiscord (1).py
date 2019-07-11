import random
import discord
import logging
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import os
import asyncio


bot = commands.Bot(command_prefix='$')

class Chat_bot():

    def __init__(self, jokes, greetings, avatar, name):
        self.jokes = jokes
        self.greetings = greetings
        self.avatar = avatar
        self. name = name

    def greeting(self):
        global ace_greetings
        print(self.name,":", random.choice(self.greetings))
        choice = input("\n{}: wanna hear some jokes? ".format(self.name))
        if 'y' in choice:
            self.tell_joke()
        elif choice == "no":
            print('see ya later!')
            exit()
        else:
            print("I cant understand ya baby")

    def tell_joke(self):
        global ace_jokes
        print(random.choice(self.jokes))
        choice = input("\n{}: Wanna hear another joke? ".format(self.name))
        if 'y' in choice:
            self.tell_joke()
        elif choice =='no':
            print('see ya later baby!')
        else:
            print("I cant understand ya!")
            

    
ace_greetings = []
ace_greetings_file = open("ace_greetings.txt", "r")
ace_jokes = []
ace_jokes_file = open("ace_jokes.txt","r")
ace_wisdom = []
ace_wisdom_file = open("ace_wisdom.txt","r")

for wisdom in ace_wisdom_file:
    ace_wisdom.append(wisdom)

for jokes in ace_jokes_file:
    ace_jokes.append(jokes)

for greeting in ace_greetings_file:
    ace_greetings.append(greeting)

ace_visconti = Chat_bot(ace_jokes, ace_greetings, False, "Ace Visconti" )


logging.basicConfig(level = logging.INFO)

@bot.command()
async def join(self, ctx, *, channel: discord.VoiceChannel):
    """Joins a voice channel"""
    print('this is running')
    if ctx.voice_client is not None:
        return await ctx.voice_client.move_to(channel)
    await channel.connect()        




class my_client(discord.Client):



    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        for guild in client.guilds:
            for channel in guild.channels:
                if channel.name == 'general':
                    await channel.send('Hey baby! I got four commands!\n /jokes \n /wisdom \n /hello \n /help')


        
    async def on_message(self, message):
        if message.author == client.user:
            return
        print('Message from {0.author}: {0.content}'.format(message))

        if message.content.startswith('/joke'):
            await message.channel.send("Ace Visconti Says: {}".format(random.choice(ace_jokes)))
        if message.content.startswith('/hello'):
            await message.channel.send(random.choice(ace_greetings))
        if message.content.startswith('/wisdom'):
            await message.channel.send("Like Ace Visconti Always Says: {}".format(random.choice(ace_wisdom)))
        if message.content.startswith('/help'):
            await message.channel.send("Hey baby! I got four commands!\n /jokes \n /wisdom \n /hello \n /help")

    @bot.command(pass_context=True, aliases=['l','lea'])
    async def leave(ctx):
        channel = ctx.message.author.voice.channel
        voice = get(bot.voice_clients, guild = ctx.guild)

        if voice and voice.is_connected():
                 await voice.disconnect()
                 print(f"See ya!")
                 await ctx.send(f"im gone bro")
        else:
            print('Bot dindt leave')
            await ctx.send("dont think I can leave")
    
client = my_client()
client.run('NTk4NzExMzkzNTAzNTQzMzE2.XSdrNg.x31NecVvtL0oANeLzeTAFwHGLeo')





