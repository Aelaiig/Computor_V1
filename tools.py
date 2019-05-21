import re

def simplifier(equation):
    # simple = ""
    # j = 0
    # i = 0
    # len_equation = len(equation)
    # while i + 1 < len_equation :
    #     # if equation[i].isnumeric and i == 0 and equation[i+1] == ' ':
    #     #     simple[j] = 'X'
    #     #     simple[j+1] = '^'
    #     #     simple[j+2] = '0'
    #     #     i + 1

    #     # # if equation[i].isnumeric and i != 0 and
    #     # simple[j] = equation[i]
    #     print(equation[i])
    #     i += 1
    #     j + 1
    simple = re.sub("(^|[ +=-])(\d+(?:(\.\d+)?))($|[ ][^\*])", r" \2 * X^0\4", equation)
    simple2 = re.sub("([\+\-\=]|^)\s*[X]([\s*]|$)", r"\1 1 * X^1 ", simple)
    print('simple' + simple, '\n', simple2, '\n')
    return simple2


    # avant . X^
    # apres espace
    #