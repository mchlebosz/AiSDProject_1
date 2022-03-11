from math import factorial


def generate2(start, end, step):
    outArray = []
    while start < end:
        outArray.append(start)
        start += step
        step += step
    return outArray


def generate1(start, end, step):
    return list(range(start, end, step))


def generate3(start, end, step):
    return [factorial(i) for i in range(start, end, step)]
