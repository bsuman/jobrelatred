# You're about to go on a trip around the world! On this trip you're bringing your trusted backpack, that anything fits into.
# The bad news is that the airline has informed you that your luggage cannot exceed a certain amount of weight.
#
# To make sure you're bringing your most valuable items on this journey you've decided
# to give all your items a score that represents how valuable this item is to you.
# It's your job to pack your bag so that you get the most value out of the items that you decide to bring.
#
# Your input will consist of two arrays, one for the scores and one for the weights.
# Your input will always be valid lists of equal length, so you don't have to worry about verifying your input.
#
# You'll also be given a maximum weight. This is the weight that your backpack cannot exceed.
#
# For instance, given these inputs:
#
# scores = [15, 10, 9, 5]
# weights = [1, 5, 3, 4]
# capacity = 8
# The maximum score will be 29. This number comes from bringing items 1, 3 and 4.
#
# Note: Your solution will have to be efficient as the running time of your algorithm will be put to a test.

def pack_bagpack(scores, weights, capacity):
    combi = [None for i in range(capacity +1)]
    dict = {}
    for i in range(len(weights)):
        if weights[i] in dict.keys():
            if dict[weights[i]] < scores[i]:
                dict[weights[i]] = scores[i]
        else:
            dict[weights[i]] = scores[i]

    combi[0] = [[]]
    weightset = set(weights)
    for i in range(len(combi)):
        if combi[i] is not None:
            for j in weightset:
                if j != i:
                    for k in combi[i]:
                        if j not in k:
                            new = k + [j]
                            if i+j < len(combi):
                                if combi[i+j] is not None:
                                    combi[i+j] = combi[i+j] + [new]
                                else:
                                    combi[i + j] = [new]

    maxscore = 0
    counter = capacity
    while counter >= 0:
        combination = combi[counter]
        if combination is not None:
            for i in combination:
                currscore = 0
                for j in i:
                    currscore = currscore + dict[j]
                    if maxscore < currscore:
                        maxscore = currscore
        counter = counter - 1

    return maxscore

if __name__ == '__main__':
    #print(pack_bagpack([20, 5, 10, 40, 15, 25], [1, 2, 3, 8, 7, 4], 10))
    #print(pack_bagpack([15, 10, 9, 5], [1, 5, 3, 4], 8))
    #scores = [15, 10, 9, 5]
    #weights = [1, 5, 3, 4]
    #capacity = 8
    #print(pack_bagpack(scores, weights, capacity))
    #scores = [100, 5, 16, 18, 50]
    #weights = [25, 1, 3, 2, 15]
    #capacity = 14
    #print(pack_bagpack(scores, weights, capacity))
    scores =[15, 13, 6, 8, 8, 7, 11, 4, 17, 19, 15, 11, 20, 20, 5, 18, 8]
    weights = [4, 1, 3, 5, 4, 2, 1, 5, 5, 2, 2, 1, 1, 4, 5, 1, 1]
    capacity = 14
    print(pack_bagpack(scores, weights, capacity))