def nested(brackets):
    openers = ['(', '{', '[']
    closers = [')', '}', ']']
    pairs = dict(zip(closers, openers))
    read = ''
    for bracket in brackets:
        if bracket in openers:
            read += bracket
        elif bracket in closers:
            if pairs[bracket] == read[-1]:
                read = read[:-1]
            else:
                return False
        else:
            continue
    return True



print nested("{ [ ] ( ) }")
# True
print nested("{ [ ( ] ) }")
# False
print nested("\{ [ \}")
# False
