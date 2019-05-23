import re

def simplifier(equation):
    simple = re.sub(r"(^|[ +=-])(\d+(?:(\.\d+)?))($|[ ][^\*])", r" \2 * X^0\4", equation)
    simple2 = re.sub(r"([\+\-\=]|^)\s*[X]([\s*]|$)", r"\1 1 * X^1 ", simple)
    simple3 = re.sub(r"([^\*]|^)([ ]|^)([X][\^])", r"\1 1 * \3", simple2)
    # print('simple',  simple, '\n', simple2, '\n', simple3, '\n')
    return simple3

def ft_ftoa(number):
    ret = str(number)
    ln = len(ret)
    check = ret[ln - 2:]
    if check == ".0":
        return ret[:ln - 2]
    return ret
