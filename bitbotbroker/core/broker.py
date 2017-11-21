# This class is your personal broker. It decides wether to buy or sell bitcoins depending on the selected algorithm. It also keeps track of all the euros and bitcoins the user has
class broker:
    eurWallet = 0 # Amount of available euros
    btcWallet = 0 # Amount of available bitcoins
    totalWallet = 0 # Total amount of euros plus exchanged bitcoins
    totalWalletAtStart = 0 # Original total wallet at start of the program
    mode = "test" # Mode of run. Test mode uses local files as wallets and performs operations in test mode. No real money is used
    stats = None # Broker needs to know the current stats.
    eurWalletTestFile = "" 
    btcWalletTestFile = ""
    numberOfBuys = 0
    numberOfSells = 0

    def __init__(self, stats, eur, btc, mode = "test"):
        self.mode = mode
        self.stats = stats
        numberOfBuys = 0
        numberOfSells = 0

        if self.mode == "test":
            self.eurWalletTestFile = eur
            self.btcWalletTestFile = btc
            self.readWalletsTest()

# Reads test wallet, which are local files with amount of euros and bitcoins
    def readWalletsTest(self):
        file = open(self.eurWalletTestFile, "r") 
        self.eurWallet = float(file.read())
        file.close()

        file = open(self.btcWalletTestFile, "r") 
        self.btcWallet = float(file.read())
        file.close()
        
        self.totalWalletAtStart = self.eurWallet + self.btcWallet * self.stats.currentRate

# When a test buy/sell operation is performed, this method writes the current value of euros and bitcoins into a local file
    def writeWalletsTest(self):
        file = open(self.eurWalletTestFile, "w") 
        file.write(str(self.eurWallet))
        file.close()

        file = open(self.btcWalletTestFile, "w") 
        file.write(str(self.btcWallet))
        file.close()

# This method buys a certain amount of bitcoins. Results are not persistant, it only updates memory
    def buy(self, quantity):
        if self.eurWallet >= quantity:
            self.btcWallet = self.btcWallet + quantity/self.stats.currentRate
            self.eurWallet = self.eurWallet - quantity
            self.numberOfBuys += 1

        if self.mode == "test":
            self.writeWalletsTest()
        
# This method sells a certain amount of bitcoins. Results are not persistant, it only updates memory
    def sell(self, quantity):
        if self.btcWallet >= quantity:
            self.eurWallet = self.eurWallet + quantity * self.stats.currentRate
            self.btcWallet = self.btcWallet - quantity
            self.numberOfSells += 1

        if self.mode == "test":
            self.writeWalletsTest()

# Method that prints current values of wallets plus the total (at current exchange rate) as well as calculates the current benefit from when the program was started up until now
    def printWallets(self):
        print("Euros: " + str(self.eurWallet))
        print("Btc: " + str(self.btcWallet)) 
        print("Total in euros: " + str(self.totalWallet)) 
        print("Total Benefit in euros: " + str(self.totalWallet - self.totalWalletAtStart)) 
        print("Number of buy operations: " + str(self.numberOfBuys)) 
        print("Number of sell operations: " + str(self.numberOfSells)) 

    def __str__(self):
        returnString = (
        "Euros: " + str(self.eurWallet) + "\n" +
        "Btc: " + str(self.btcWallet) + "\n" +
        "Total in euros: " + str(self.totalWallet) + "\n" +
        "Total Benefit in euros: " + str(self.totalWallet - self.totalWalletAtStart) + "\n" +
        "Number of buy operations: " + str(self.numberOfBuys) + "\n" +
        "Number of sell operations: " + str(self.numberOfSells))
        return returnString
