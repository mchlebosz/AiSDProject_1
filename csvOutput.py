import csv


def create(filename, outputData):
    with open(filename+'.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Amount", "Random", "Increasing",
                        "Decreasing", "Constant", "ASpread"])
        for amount in outputData:
            timingData = outputData[amount].values()
            writer.writerow([amount] + list(timingData))


def createMultiple(filename, amount, outputDatas):
    with open(filename+'.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for i in range(amount):
            writer.writerow(["Amount", "Random", "Increasing",
                            "Decreasing", "Constant", "ASpread"])
            for amount in outputDatas[i]:
                timingData = outputDatas[i][amount].values()
                writer.writerow([amount] + list(timingData))
            writer.writerow(["", "", "",
                            "", "", ""])
