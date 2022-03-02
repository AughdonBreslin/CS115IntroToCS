def knapsack(capacity, itemlist):
    if capacity <= 0 or itemlist == []:
        return [0, []]
    elif capacity < itemlist[0][0]:
        return knapsack(capacity, itemlist[1:])
    else:
        use = knapsack(capacity-itemlist[0][0], itemlist[1:])
        use[0] += itemlist[0][1]
        use[1] = [itemlist[0]] + use[1]
        lose = knapsack(capacity, itemlist[1:])
        if use[0] > lose[0]:
            return use
        else:
            return lose
