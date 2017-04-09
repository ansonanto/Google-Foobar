def combinations(q, n):
    answer = []
    i = 1
    while i <= n:
        answer.extend(branches(q - n, i, q, [i]))
        i += 1
    return answer

def branches(bunniesLeft, currentBranch, rabbitsLeft, items):
    if bunniesLeft == 0:
        return [items]
    if bunniesLeft > 0 and currentBranch <= rabbitsLeft:
        i = currentBranch + 1
        accumulated = []
        highestBranchValue = rabbitsLeft - bunniesLeft + 1
        while i <= highestBranchValue:
            nextArray = items[:]
            nextArray.append(i)
            accumulated.extend(branches(bunniesLeft - 1, i, rabbitsLeft, nextArray))
            i += 1
        return accumulated
    
def answer(num_buns, num_required):
    combi = combinations(num_buns, num_required)
    minionsList = [[] for q in range(num_buns)]
    for index, item in enumerate(combi):
        for key in item:
            minionsList[key-1].append(index)
    return minionsList