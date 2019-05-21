import re

def simplifier2(item):
    if item.isnumeric():
        new_item = item + " * X^0"
        return new_item
    elif item == 'X':
        return item.replace('X', '1 * X^1')
    elif item[0] == 'X' and item[1] == '^':
        new_item = "1 * " + item
        return new_item
    else :
        return item

def simplifier(equation):
    tab = re.split(' ', equation)
    mapping = list(map(simplifier2, tab))
    simple = ' '.join(mapping)
    return simple

def ft_ftoa(number):
    ret = str(number)
    ln = len(ret)
    check = ret[ln - 2:]
    if check == ".0":
        return ret[:ln - 2]
    return ret
