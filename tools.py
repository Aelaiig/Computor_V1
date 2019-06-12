import re

def simplifier(equation):
    equ = re.sub(r"(^|[\=\+\-])\s*(\d+(?:\.\d+)?)\s*\*?\s*X\s*\^?\s*(\d+)\s*(?=[\+\-\=]|$)", r"\1 \2 * X^\3 ", equation) # NXN || N*XN || NX^N => N * X^N
    simple = re.sub(r"(^|[ +=-])(\d+(?:(\.\d+)?))($|[ ][^\*])", r" \2 * X^0\4", equ) # case X alone
    simple2 = re.sub(r"([\+\-\=]|^)\s*[X]([\s*]|$)", r"\1 1 * X^1 ", simple) # case N alone
    simple3 = re.sub(r"([^\*]|^)([ ]|^)([X][\^])", r"\1 1 * \3", simple2) # case X^N
    # print('simple',  simple, '\n', simple2, '\n', simple3, '\n')
    return simple3

def ft_ftoa(number):
    ret = str(number)
    ln = len(ret)
    check = ret[ln - 2:]
    if check == ".0":
        return ret[:ln - 2]
    return ret


def sqrt(number):
    i = 0
    while i < number :
        if (i * i) == number:
            return i
        i += 0.00000001
    return 0
