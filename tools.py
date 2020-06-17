import re

def simplifier(equation):
    equ = re.sub(r"(^|[\=\+\-])\s*(\d+(?:\.\d+)?)\s*\*?\s*X\s*\^?\s*(\d+)\s*(?=[\+\-\=]|$)", r"\1 \2 * X^\3 ", equation) # NXN || N*XN || NX^N => N * X^N
    simple = re.sub(r"(^|[ +=-])(\d+(?:(\.\d+)?))($|[ ][^\*])", r" \2 * X^0\4", equ) # case X alone
    simple2 = re.sub(r"([\+\-\=]|^)\s*[X]([\s*]|$)", r"\1 1 * X^1 ", simple) # case N alone
    simple3 = re.sub(r"([^\*]|^)([ ]|^)([X][\^])", r"\1 1 * \3", simple2) # case X^N
    return simple3

def ft_ftoa(number):
    ret = str(number)
    ln = len(ret)
    check = ret[ln - 2:]
    if check == ".0":
        return ret[:ln - 2]
    return ret

def ft_round(x) :
    s = str(x)
    j = s.find(".")
    if j == -1 :
        return(x)
    round = s[:j + 5]
    return (float(round))

# sqrt: x = (x + x/delta)/2 Algorithme de Babylone, Méthode de Héron 

def sqrt(x, delta, prevResult, i):
    if (i < 1000): # to avoid too long calcul
        i += 1
        x = (x + delta / x)/2
        if x == prevResult:
            return (ft_round(x))
        else:
            return sqrt(x, delta, x, i)
    else:
        return (ft_round(x))
