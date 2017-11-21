import time
import telepot
from telepot.loop import MessageLoop

# This class is in charge of listening to messages that come from the telegrambot and answering them. It is called concurrent because it runs as aparallel thread to the program, and answers the user inmediatelly.
class telegrambotConcurrent:
    bot = None # Used for creating an instance of the telepot library
    broker = None # Our bot needs access to the broker to get all the data
    stats = None # Our bot needs access to the stats to get all the info
    telegramUsersFile = None # This is the file where we save all users that are currently subscribed to the bot. If a user is subscribed/authenticated.
    subscribedUsers = [] # List of currently subscribed users
    telegramSubscribePassword = "" # Password for subscribing to the bot, read from config file.

    def __init__(self, token, telegramUsersFile, telegramSubscribePassword, stats, broker):
        self.token = token
        self.bot = telepot.Bot(token) # Bot is created from the telepot class
        self.broker = broker
        self.stats = stats
        self.telegramUsersFile = telegramUsersFile
        self.telegramSubscribePassword = telegramSubscribePassword
        self.readUsers()
        MessageLoop(self.bot, self.handle).run_as_thread()

# This method creates a string with all the data of the stats and broker. This can be consumed by the bot to send it to the user
    def printData(self):
        returnString =(
        "##############################" + "\n" +
        time.strftime("%d/%m/%Y") + "\n" +
        time.strftime("%H:%M:%S") + "\n" +
        str(self.stats) + "\n" +
        str(self.broker) + "\n" +
        "##############################")
        return returnString

# This method reads the file of subscribed users and fills in the self.subscribedUsers which contains subscribed users in memory.
    def readUsers(self):
        del self.subscribedUsers[:] # We empty the subscribed user list first 

        file = open(self.telegramUsersFile, "r")
        for user in file:
            self.subscribedUsers.append(user.replace("\n", "")) # This loop fills in the subscribedusers, removing the \n at the end of each line
        file.close()

# This method makes the subscribed users persistent. It writes all users into a file.
    def writeUsers(self):
        file = open(self.telegramUsersFile, "w")

        for user in self.subscribedUsers:
            file.write(str(user)+"\n") 
        file.close()

# This method checks if a user is subscribed or not.
    def checkSubscribed(self, user):
        if user in self.subscribedUsers:
            return True
        else:
            return False

# This method is called everytime the bot receives a message. It then dispatches it depending on what the user has sent.
    def handle(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
    
        if content_type == 'text' :
            if msg['text'] == "/data":
                self.sendData(msg)

            if msg['text'] == "/subscribe " + self.telegramSubscribePassword: 
                self.subscribe(msg)

# This method implemets the petition of asking for current data in the broker/stats
    def sendData(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)

        if self.checkSubscribed(str(msg['from']['id'])):
            self.bot.sendMessage(chat_id, self.printData())

# This method subscribes a user to the list of subscribed user. Once a user is subscribed (he needs to enter a password) he will be able to ask more queries.
    def subscribe(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        userId = str(msg['from']['id'])

        if userId not in self.subscribedUsers:
            self.subscribedUsers.append(userId)
            self.writeUsers()
            self.readUsers()
            self.bot.sendMessage(chat_id, "User " + userId + " subscribed")
        else:
            self.bot.sendMessage(chat_id, "User " + userId + " was already subscribed")

