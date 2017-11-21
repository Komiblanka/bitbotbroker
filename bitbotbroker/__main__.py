import argparse # This is used to parse arguments from command line.
from configparser import SafeConfigParser
from stats import *
from core import *
from notifiers import *
import time
import os
import sys

# This global function calls all the printing methods as well as clearing the screen
def printAll(stats, broker):
    os.system("clear")
    print(printData(stats, broker))


def printData(stats, broker):
    returnString =(
    "##############################" + "\n" +
    time.strftime("%d/%m/%Y") + "\n" +
    time.strftime("%H:%M:%S") + "\n" +
    str(stats) + "\n" +
    str(broker) + "\n" +
    "##############################")
    return returnString

# Main starts here
# Argument parsing.
parser = argparse.ArgumentParser(description='Welcome to your bitbotbroker')
 
parser.add_argument('configFile', help='Config file for loading all parameters')
args = parser.parse_args()

# Using config file for parameters
parser = SafeConfigParser()
parser.read(args.configFile)

eurFile = parser.get('wallets', 'eur_wallet_file')
btcFile = parser.get('wallets', 'btc_wallet_file')
executionMode = parser.get('execution_options', 'mode')
telegramFlag = parser.get('notifiers', 'use_telegram')

if telegramFlag == "True":
    useTelegram = True
    telegramToken = parser.get('notifiers', 'telegram_token')
    telegramUsersFile = parser.get('notifiers', 'telegram_users_file')
    telegramSubscribePassword = parser.get('notifiers', 'telegram_subscribe_password')

# Creation of stat object and broker. It is important to update stats before assigning it to the broker, as the initial wallet depends on the stats value
myStats = bitstampStats()
myStats.update()
myBroker = broker(myStats, eurFile, btcFile, executionMode)

# Declaring the telegrambot
if useTelegram:
    myBot = telegrambotConcurrent(telegramToken, telegramUsersFile, telegramSubscribePassword, myStats, myBroker)

# Iteration object used for knowing how many iterations of the while has been made
iteration = 0
myAlgorithm = brokerBehaviour()

while(1):
    myStats.update()
    myAlgorithm.usePercentageAlgorithm(myBroker, 0.2, 1)
    printAll(myStats, myBroker)
    print("")
    print("Iteration: " + str(iteration))
    iteration += 1
    
    if useTelegram:
        print("Using telegram")

    time.sleep(60)
