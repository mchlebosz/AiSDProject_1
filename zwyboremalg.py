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
    print("wpisz: insertion,selection,shell,heap,quickR,quickL")
    k=input()
    print("wpisz:Random,Increasing,Decreasing,ASpread,Constant")
    z=input()
    print(z)

    print("podaj długość ciągu")
    amounts = [int(input())]

    inputData = dataGen.generateTestingData(amounts)
    print(inputData[amounts[0]][z])
    print("Generated Data")

    print("Starting sorting")

    for amount in inputData:


        for spread, values in inputData[amount].items():
            if k=="insertion":
                timeStart = time.time()
                insertion.sort(values)
                timeDiff = time.time() - timeStart

            elif k=="shell":
                timeStart = time.time()
                shell.sort(values)
                timeDiff = time.time() - timeStart

            elif k=="selection":
                timeStart = time.time()
                selection.sort(values)
                timeDiff = time.time() - timeStart

            elif k=="heap":
                timeStart = time.time()
                heap.sort(values)
                timeDiff = time.time() - timeStart

            elif k=="quickL":
                timeStart = time.time()
                quick.sortLeft(values)
                timeDiff = time.time() - timeStart

            else:
                timeStart = time.time()
                quick.sortRand(values)
                timeDiff = time.time() - timeStart


    print("All Sorted")
    print(inputData[amounts[0]][z])
