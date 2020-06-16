import re
import verbose as v

def simply(equa):

    # splitter en 2 avec le "="
    splitted = re.split("=", equa)

    # si il n'y a pas de "=" c'est pas une equation
    if len(splitted) == 1 :
        v.ft_missing_equal()

    #### Creation de variables ###
    #liste ou on stock les nombres (valeur) en fonction de leur puissance (cle)
    numbers = {} 
    #pattern pour recuperer les differents polynomes
    pattern = re.compile("(\-?\s*\d+(?:\.\d+)?)\s*\*\s*X\^(\d+)")

    #recuperation et symplification des polynomes cote gauche du "="
    match = re.findall(pattern, splitted[0])
    for polynome in match:
        value =  float(polynome[0].replace(' ', ''))
        power = int(polynome[1].replace(' ', ''))
        if value != 0:
            try :
                numbers[power] += value
            except KeyError:
                numbers[power] = value

    #recuperation et symplification des polynomes cote droit du "="
    match = re.findall(pattern, splitted[1])
    for polynome in match:
        value =  float(polynome[0].replace(' ', ''))
        power = int(polynome[1].replace(' ', ''))
        if value != 0:
            try :
                numbers[power] -= float(value)
            except KeyError:
                numbers[power] = -float(value)
    #filter null value
    filterNumbers = {}
    for power, value in numbers.items():
        if value != 0:
            filterNumbers[power] = value
    return(filterNumbers)