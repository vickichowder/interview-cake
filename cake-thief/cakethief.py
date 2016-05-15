def max_duffel_bag_value(cakes, capacity):
    cakes = [(weight, value) for (weight, value) in cakes if weight < capacity]
    print([value/weight for (weight, value) in cakes])
    cakes = sorted(cakes, key=lambda cake: (cake[1]/cake[0]), reverse=True)
    print(cakes)
    print([value/weight for (weight, value) in cakes])

    # print('Number of cakes eligible for heist: {}'.format(len(cakes)))
    remaining = capacity
    stole = 0
    # Grab as many most expensive ones as possible
    for cake in cakes:
        if cake[0] <= remaining:
            cakes_stolen = remaining/cake[0]
            print('Stealing {} cakes of weight {}'.format(cakes_stolen, cake[0]))
            stolen_value = cakes_stolen * cake[1]
            stole += stolen_value
            remaining -= cakes_stolen * cake[0]
            print('Remaining weight left in duffle: {}'.format(remaining))
        else:
            next
    print('-----------------------')
    print('Stole {} worth of cakes'.format(stole))


cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity1   = 20
capacity2 = 5

max_duffel_bag_value(cake_tuples, capacity1)
# return 555
# max_duffel_bag_value(cake_tuples, capacity2)
# return 105
