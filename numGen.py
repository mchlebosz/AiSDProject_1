import random

# number generating algorithms
# I modified to generate float numbers


# numbers in decreasing order
# amount: amount of numbers in the output array
# minimum: smallest number in the set
# maximum: biggest number in the set
def Decreasing(amount, minimum=0, maximum=None):

    if maximum == None:
        maximum = amount
    if minimum >= maximum:
        print("Range Error: minimum cannot be bigger than maximum")

    outArray = [random.uniform(minimum, maximum) for i in range(amount)]
    outArray.sort(reverse=True)
    return outArray

# numbers in increasing order
# amount: amount of numbers in the output array
# minimum: smallest number in the set
# maximum: biggest number in the set


def Increasing(amount, minimum=0, maximum=None):

    if maximum == None:
        maximum = amount
    if minimum >= maximum:
        print("Range Error: minimum cannot be bigger than maximum")
    outArray = [random.uniform(minimum, maximum) for i in range(amount)]
    outArray.sort()
    return outArray

# numbers in ASpread order
# amount: amount of numbers in the output array
# minimum: smallest number in the set
# maximum: biggest number in the set


def ASpread(amount, minimum=0, maximum=None):
    if maximum == None:
        maximum = amount
    if minimum >= maximum:
        print("Range Error: minimum cannot be bigger than maximum")

    outArray1 = [random.uniform(minimum, maximum) for i in range(amount//2)]
    outArray1.sort()
    outArray2 = [random.uniform(minimum, maximum) for i in range(amount//2)]
    outArray2.sort(reverse=True)

    return outArray1 + outArray2


# los

# numbers in ASpread order
# amount: amount of numbers in the output array
# minimum: smallest number in the set
# maximum: biggest number in the set
def Random(amount, minimum=0, maximum=None):

    if maximum == None:
        maximum = amount
    if minimum >= maximum:
        print("Range Error: minimum cannot be bigger than maximum")

    return [random.uniform(minimum, maximum) for i in range(amount)]

# stałe


def Constant(amount, value=10.1):
    return [value for i in range(amount)]


if __name__ == '__main__':
    print(Increasing(50), "\n")
    print(Decreasing(50), "\n")
    print(ASpread(50), "\n")
    print(Random(50), "\n")
    print(Constant(50), "\n")
