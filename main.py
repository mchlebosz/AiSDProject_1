import insertion
import shell
import selection
import quick
import heap
import numGen
import time
import amounts
import csv


def generateTestingData(amounts):
    return {
        value: {
            "Random": numGen.Random(value),
            "Increasing": numGen.Increasing(value),
            "Decreasing": numGen.Decreasing(value),
            "Constant": numGen.Constant(value),
            "ASpread": numGen.ASpread(value),
        } for value in amounts
    }


def generateOutputDict(amounts):
    return {
        value: {
            "Random": -1,
            "Increasing": -1,
            "Decreasing": -1,
            "Constant": -1,
            "ASpread": -1,
        } for value in amounts
    }


if __name__ == '__main__':
    """    outF = open("output.out", "w")
       outF.write("test") """

    dataStart = 1000
    dataStep = 1000
    dataStop = dataStep * 18 + 1

    amounts = amounts.generate1(dataStart, dataStop, dataStep)

    inputData = generateTestingData(amounts)
    print("Generated Data")
    InsertionTime = generateOutputDict(amounts)
    ShellTime = generateOutputDict(amounts)
    SelectionTime = generateOutputDict(amounts)

    print("Generated Output Dicts")

    print("Starting sorting")

    for amount in inputData:
        print(amount)
        for spread, values in inputData[amount].items():
            timeStart = time.time()
            insertion.sort(values)
            timeDiff = time.time() - timeStart
            InsertionTime[amount][spread] = timeDiff

            timeStart = time.time()
            shell.sort(values)
            timeDiff = time.time() - timeStart
            ShellTime[amount][spread] = timeDiff

            timeStart = time.time()
            selection.sort(values)
            timeDiff = time.time() - timeStart
            SelectionTime[amount][spread] = timeDiff

    print("All Sorted")

    print("Saving InsertionSort Times")
    with open('InsertionSort.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Amount", "Random", "Increasing",
                        "Decreasing", "Constant", "ASpread"])
        for amount in InsertionTime:
            timingData = InsertionTime[amount].values()
            writer.writerow([amount] + list(timingData))

    print("Saving ShellSort Times")
    with open('ShellSort.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Amount", "Random", "Increasing",
                        "Decreasing", "Constant", "ASpread"])
        for amount in ShellTime:
            timingData = ShellTime[amount].values()
            writer.writerow([amount] + list(timingData))

    print("Saving SelectionSort Times")
    with open('SelectionSort.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Amount", "Random", "Increasing",
                        "Decreasing", "Constant", "ASpread"])
        for amount in SelectionTime:
            timingData = SelectionTime[amount].values()
            writer.writerow([amount] + list(timingData))
