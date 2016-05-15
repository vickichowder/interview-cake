def riffle_check(shuffled, half1, half2):
    remaining1 = half1
    remaining2 = half2
    print(remaining1[1:])
    for card in shuffled:
        if (len(remaining1) > 0) and (card == remaining1[0]):
            if len(remaining1) >= 1:
                print(remaining1)
                remaining1 = remaining1[1:]
        elif (len(remaining2) > 0) and (card == remaining2[0]):
            if len(remaining2) >= 1:
                print(remaining2)
                remaining2 = remaining2[1:]
        else:
            print(remaining1, remaining2)
            print('Not a riffle! :O')
            return False

    return True


shuffled_deck = [1,7,2,8,3,9,4,10,5,11,6,13]
half1 = [1,2,3,4,5,6]
half2 = [7,8,9,10,11,12]
riffled = riffle_check(shuffled_deck, half1, half2)
print('Is this desk riffled? {}'.format(riffled))
