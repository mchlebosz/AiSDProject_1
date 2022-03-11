import numGen


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
