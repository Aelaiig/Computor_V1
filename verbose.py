import sys

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

    for degree in table:
        if numbers[degree] < 0:
            sign = " - "
            numbers[degree] = -numbers[degree]
        else:
            sign = " + "
        if printed == 0:
            if sign == " - ":
                to_print = to_print + sign
            to_print = to_print + str(numbers[degree]) + " * X^"+ str(degree)
            printed = 1
        else:
            to_print = to_print + sign + str(numbers[degree]) + " * X^"+ str(degree)

    print(to_print)
    print("Polynomial degree: ", table[0])
    if table[0] > 2 :
        print ("The polynomial degree is strictly greater than 2, I can't solve.")
        sys.exit()
