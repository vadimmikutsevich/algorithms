def findWinners(matches):
    winners = set()
    losers = set()
    strongLosers = set()

    for i in range(len(matches)):
        if matches[i][1] in losers:
            losers.remove(matches[i][1])
            strongLosers.add(matches[i][1])
        if matches[i][1] not in strongLosers and matches[i][1] not in losers:
            losers.add(matches[i][1])
        if matches[i][1] in winners:
            winners.remove(matches[i][1])
        
        if matches[i][0] not in losers and matches[i][0] not in strongLosers:
            winners.add(matches[i][0])

    return [sorted(list(winners)), sorted(list(losers))]


print(findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))
findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]])