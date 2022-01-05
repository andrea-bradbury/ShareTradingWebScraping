class ASX:
    def __init__(self, name, lastPrice, dividendAmount, annualReturn):
        self.name = name
        self.lastPrice = lastPrice
        self.dividendAmount = dividendAmount
        self.annualReturn = annualReturn


    def format(self):
        print(f"{self.name},\n" 
                f" Last Price: {self.lastPrice},\n"
                f" {self.dividendAmount}%,\n "
                f" {self.annualReturn}%.\n\n")
