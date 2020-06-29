def assignResult(game):
    if game.resultAway < game.resultHome:
        resultHome = 1
        resultAway = 0
    elif game.resultAway > game.resultHome:
        resultHome = 0
        resultAway = 1
    else:
        resultHome = 0.5
        resultAway = 0.5
    return [resultHome, resultAway]


def assignGoalDifferenceIndex(game):
    if abs(game.resultAway-game.resultHome) <= 1:
        retVal = 1
    elif abs(game.resultAway-game.resultHome) == 2:
        retVal = 1.5
    else:
        retVal = (11 + float(abs(game.resultAway-game.resultHome)))/8
    return retVal


def calculateExpectedResult(game):
    starDiffhome = float(game.homeTeam.rating) - float(game.awayTeam.rating)
    expResHome = 1 / (10 ** (-60 * starDiffhome / 200) + 1)
    expResAway = 1 - expResHome
    return [expResHome, expResAway]


def calculateNewPointsValue(game):
    G = assignGoalDifferenceIndex(game)
    K = 30
    [ReHome, ReAway] = calculateExpectedResult(game)
    [Rhome, Raway] = assignResult(game)
    newPointsValueforHomeUser = round(float(game.homeUser.rating.value) + K * G * (Rhome - ReHome))
    newPointsValueforAwayUser = round(float(game.awayUser.rating.value) + K * G * (Raway - ReAway))
    return [newPointsValueforHomeUser, newPointsValueforAwayUser]
