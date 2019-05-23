import sys
import tools

def ft_usage():
    print ("\n\t---------- Usage ---------- \n\n python3 main.py \"equation\" [-v]\n\t\t\"equation\": valid input, some bonus like double spaces, min x\n\t\t-v: optional, shows details of resolution\n\t\t-h: help\n")
    sys.exit()

def ft_missing_equal():
    print ("There is no \"=\" in your equation... actually it's not even an equation ><'")
    sys.exit()

def ft_simplyprint(numbers):

    #cree un tableau contenant toutes les puissances trie dans l'ordre decroissant
    table = sorted(numbers, reverse=True)
    #Cree la chaine a afficher avec l'equation simplifie
    to_print = "Reduced form: "
    printed = 0
    sign = ""
    higest = 0

    for degree in table:
        if numbers[degree] != 0:
            if numbers[degree] < 0:
                sign = " - "
                numbers[degree] = -numbers[degree]
            else:
                sign = " + "
            if printed == 0:
                if sign == " - ":
                    to_print = to_print + "-"
                to_print = to_print + tools.ft_ftoa(numbers[degree]) + " * X^"+ str(degree)
                printed = 1
            else:
                to_print = to_print + sign + tools.ft_ftoa(numbers[degree]) + " * X^"+ str(degree)
    if to_print != "Reduced form: ":
        to_print = to_print + " = 0"
    else:
        to_print += "0"
    print(to_print)
    return table[0]
