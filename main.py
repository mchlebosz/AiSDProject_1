import insertion
import shell
import selection
import quick
import heap
import dataGen
import time
import amounts
import csvOutput
import numGen


if __name__ == '__main__':
    # PreAlgorithm only for Showcase
    """ amount = int(input("Enter Amount: \n"))
    values = numGen.Random(amount)
    print(values)
    shell.sort(values)
    print("\n", values)
    exit() """

    chooseString = input("Choose which algorithms to run: \n 1. Insertion Sort \n 2. Shell Sort \n 3. Selection Sort \n 4. Heap Sort \n 5. Quick Sort (Left Pivot) \n 6. Quick Sort (Random Pivot) \n Use numbers to chose one (i.e 135 = Insertion , Selection, QuickLeft ; 123456 for all) : \n")
    dataCount = int(input("Enter amount of data points\n"))
    dataStart = 1000
    dataStep = 1000
    dataStop = dataStep * dataCount + 1

    print("Generating Input Data")

    amounts = amounts.generate1(dataStart, dataStop, dataStep)
    inputData = dataGen.generateTestingData(amounts)
    print("Generated Data")
    if "1" in chooseString:
        InsertionTime = dataGen.generateOutputDict(amounts)

    if "2" in chooseString:
        ShellTime = dataGen.generateOutputDict(amounts)

    if "3" in chooseString:
        SelectionTime = dataGen.generateOutputDict(amounts)

    if "4" in chooseString:
        HeapTime = dataGen.generateOutputDict(amounts)

    if "5" in chooseString:
        QuickLTime = dataGen.generateOutputDict(amounts)

    if "6" in chooseString:
        QuickRTime = dataGen.generateOutputDict(amounts)

    print("Generated Output Dicts")

    print("Starting sorting")

    for amount in inputData:
        print(amount)
        for spread, values in inputData[amount].items():
            if "1" in chooseString:
                timeStart = time.time()
                insertion.sort(values)
                timeDiff = time.time() - timeStart
                InsertionTime[amount][spread] = timeDiff
            if "2" in chooseString:
                timeStart = time.time()
                shell.sort(values)
                timeDiff = time.time() - timeStart
                ShellTime[amount][spread] = timeDiff
            if "3" in chooseString:
                timeStart = time.time()
                selection.sort(values)
                timeDiff = time.time() - timeStart
                SelectionTime[amount][spread] = timeDiff
            if "4" in chooseString:
                timeStart = time.time()
                heap.sort(values)
                timeDiff = time.time() - timeStart
                HeapTime[amount][spread] = timeDiff
            # because of stack size quicksort limit is 17000 numbers to sort
            if (amount <= 17000):
                if "5" in chooseString:
                    timeStart = time.time()
                    quick.sortLeft(values)
                    timeDiff = time.time() - timeStart
                    QuickLTime[amount][spread] = timeDiff
                if "6" in chooseString:
                    timeStart = time.time()
                    quick.sortRand(values)
                    timeDiff = time.time() - timeStart
                    QuickRTime[amount][spread] = timeDiff

    print("All Sorted")
    if "1" in chooseString:
        print("Saving InsertionSort Times")
        csvOutput.create("InsertionSort", InsertionTime)
    if "2" in chooseString:
        print("Saving ShellSort Times")
        csvOutput.create("ShellSort", ShellTime)
    if "3" in chooseString:
        print("Saving SelectionSort Times")
        csvOutput.create("SelectionSort", SelectionTime)
    if "4" in chooseString:
        print("Saving HeapSort Times")
        csvOutput.create("HeapSort", HeapTime)
    if "5" in chooseString:
        print("Saving QuickSort (Left Pivot) Times")
        csvOutput.create("QuickSortLeft", QuickLTime)
    if "6" in chooseString:
        print("Saving QuickSort (Random Pivot) Times")
        csvOutput.create("QuickSortRandom", QuickRTime)

    print("Saving Completed")
