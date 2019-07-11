import random

class Chat_bot():

    def __init__(self, jokes, greetings, avatar):
        self.jokes = jokes
        self.greetings = greetings
        self.avatar = avatar

    def greeting(self):
        global ace_greetings
        print(random.choice(self.greetings))
        choice = input("\nwanna hear some jokes? ")
        if choice == 'yes':
            self.tell_joke()
        elif choice == "NO":
            print('see ya later!')
            exit()
        else:
            print("I cant understand ya baby")

    def tell_joke(self):
        global ace_jokes
        print(random.choice(self.jokes))
        choice = input("\nWanna hear another joke?")
        if choice == 'yes':
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

ace_visconti = Chat_bot(ace_jokes, ace_greetings, False )


ace_visconti.greeting()




