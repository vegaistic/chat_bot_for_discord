import random
import discord
import logging

logging.basicConfig(level = logging.INFO)



class my_client(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        

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

for jokes in ace_jokes_file:
    ace_jokes.append(jokes)

for greeting in ace_greetings_file:
    ace_greetings.append(greeting)

ace_visconti = Chat_bot(ace_jokes, ace_greetings, False, "Ace Visconti" )


ace_visconti.greeting()




