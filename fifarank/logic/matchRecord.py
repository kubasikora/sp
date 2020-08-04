def homeUserWon(match):
    return match.resultHome > match.resultAway
 
def awayUserWon(match):
    return match.resultHome < match.resultAway
 
def drawnMatch(match):
    return match.resultHome == match.resultAway

def getUserRecord(matchList, user):
    won = 0
    drawn = 0
    lost = 0

    for match in matchList:
        if homeUserWon(match):
            if match.homeUser == user:
                won += 1
            else:
                lost += 1
        if awayUserWon(match):
            if match.awayUser == user:
                won += 1
            else:
                lost += 1
        if drawnMatch(match):
            drawn +=1   

    return (won, drawn, lost)
