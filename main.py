import insertion
import shell
import selection
import quick
import heap
import dataGen
import time
import amounts
import csvOutput


if __name__ == '__main__':
    """    outF = open("output.out", "w")
       outF.write("test") """

    dataStart = 1000
    dataStep = 1000
    dataStop = dataStep * 18 + 1

    amounts = amounts.generate1(dataStart, dataStop, dataStep)

    inputData = dataGen.generateTestingData(amounts)
    print("Generated Data")
    InsertionTime = dataGen.generateOutputDict(amounts)
    ShellTime = dataGen.generateOutputDict(amounts)
    SelectionTime = dataGen.generateOutputDict(amounts)
    HeapTime = dataGen.generateOutputDict(amounts)
    QuickLTime = dataGen.generateOutputDict(amounts)
    QuickRTime = dataGen.generateOutputDict(amounts)

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

            timeStart = time.time()
            selection.sort(values)
            timeDiff = time.time() - timeStart
            HeapTime[amount][spread] = timeDiff
            """
            timeStart = time.time()
            quick.sortLeft(values)
            timeDiff = time.time() - timeStart
            QuickLTime[amount][spread] = timeDiff

            timeStart = time.time()
            quick.sortRand(values)
            timeDiff = time.time() - timeStart
            QuickRTime[amount][spread] = timeDiff """

    print("All Sorted")

    print("Saving InsertionSort Times")
    csvOutput.create("InsertionSort", InsertionTime)

    print("Saving ShellSort Times")
    csvOutput.create("ShellSort", ShellTime)

    print("Saving SelectionSort Times")
    csvOutput.create("SelectionSort", SelectionTime)

    print("Saving HeapSort Times")
    csvOutput.create("HeapSort", HeapTime)

    print("Saving QuickSort Times")
    #csvOutput.create("QuickSort", QuickLTime)

    #csvOutput.createMultiple("QuickSort", 2, [QuickLTime, QuickRTime])

    print("Saving Completed")
