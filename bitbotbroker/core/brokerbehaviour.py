# This class defines a set of behaviours for the broker class. You can create a brokerBehaviour object and call the desired behaviour by passing to it the broker and the different required parameters
class brokerBehaviour:

# This algorithm spends a percentage of euros in bitcoins when bitoin value raises a certain percentage. It sells a percentage of bitcoins if there is a certain percentage decrease of the value of bitcoins.
    def usePercentageAlgorithm(self, broker, percentageIncrease, percentageSpend):

        if broker.stats.accumulatedBtcPercentIncrease >= percentageIncrease and broker.btcWallet > 0:
            percentageBtc = broker.btcWallet * percentageSpend/100
            broker.sell(percentageBtc)
            broker.stats.accumulatedBtcPercentIncrease = 0

        if broker.stats.accumulatedBtcPercentIncrease <= -1 *  percentageIncrease and broker.eurWallet > 0:
            percentageEur = broker.eurWallet * percentageSpend/100
            broker.buy(percentageEur)
            broker.stats.accumulatedBtcPercentIncrease = 0

        broker.totalWallet = broker.eurWallet + broker.btcWallet * broker.stats.currentRate

# This algorithm spends all euros in  bitcoin when the value increase of bitcoin increases a certain percentage (indicated to the algorithm as a parameter). It sells all bitcoins if there is a certain percentage decrease of the value of bitcoins
    def useAllAlgorithm(self, broker, percentage):
        if broker.stats.accumulatedBtcPercentIncrease >= percentage and broker.btcWallet > 0:
            broker.sell(broker.btcWallet)
            broker.stats.accumulatedBtcPercentIncrease = 0

        if broker.stats.accumulatedBtcPercentIncrease <= -1 *  percentage and broker.eurWallet > 0:
            broker.buy(broker.eurWallet)
            broker.stats.accumulatedBtcPercentIncrease = 0

        broker.totalWallet = broker.eurWallet + broker.btcWallet * broker.stats.currentRate
