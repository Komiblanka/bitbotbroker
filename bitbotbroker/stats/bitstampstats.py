import bitstamp.client
from bitstamp.client import BitstampError
import time

# This class queries bitcoin page and also calculates stats regarding the page
class bitstampStats:
    currentRate = 0 # Current exchange rate
    publicClient = bitstamp.client.Public() # Object for querying bitstamp page
    btcPercentIncrease = 0.0 # Percentage increase in bitcoin rate. Takes only into consideration the last value and the current value.
    lastRate = 0.0 # Value of the exchange before the current exchange
    accumulatedBtcPercentIncrease = 0.0 # Increase in bitcoin value since last buy/sell operation. Resets with every buy/sell operation

    def __init__(self):
        self.currentRate = 0
        accumulatedBtcPercentIncrease = 0.0 

# This method updates the current value of bitcoin. Additionally, it updates the percentages.
    def update(self):
        try:
            self.currentRate = float(self.publicClient.ticker(quote='eur')['last']) # Bitstamp query
            if self.lastRate != 0: # Checking that the lastRate is not 0 to avoid dividing by 0
                self.btcPercentIncrease = self.currentRate/self.lastRate * 100 - 100
                self.accumulatedBtcPercentIncrease = self.accumulatedBtcPercentIncrease + self.btcPercentIncrease 

            self.lastRate = self.currentRate

        except bitstamp.client.BitstampError as e:
            print("Bitstamp error: " + str(e))

# This method prints out all important stats and values for the bitcoin page
    def printStats(self):
        print (time.strftime("%d/%m/%Y"))
        print (time.strftime("%H:%M:%S"))
        print("Current rate: " + str(self.currentRate))
        print("Current increase: " + str(self.btcPercentIncrease) + "%")
        print("Accumulated increase: " + str(self.accumulatedBtcPercentIncrease) + "%")
        print("Last rate: " + str(self.lastRate))

    def __str__(self):
        returnString = (
        "Current rate: " + str(self.currentRate) + "\n" +
        "Current increase: " + str(self.btcPercentIncrease) + "%" + "\n" +
        "Accumulated increase: " + str(self.accumulatedBtcPercentIncrease) + "%" + "\n"  +
        "Last rate: " + str(self.lastRate) + "\n") 
        return returnString
