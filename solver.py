import verbose as v
import sys
import tools

def degree_zero(polynomes):
    print("Polynomial degree: 0")
    ret = polynomes.get(0, 0)
    if ret == 0:
        print ("All reals numbers are a solution for this equation")
    else:
        print("There is no solution for this equation")

def degree_one(polynomes):
    print("Polynomial degree: 1")
    b = polynomes.get(1, 0)
    c = polynomes.get(0, 0)
    if c == 0:
        v.verbose("[Verbose] bx = 0 => "+ tools.ft_ftoa(b) +"x = 0\n[Verbose] x can only be 0")
        print("The solution is:")
        print("0")
    else:
        v.verbose("[Verbose] bx + c = 0 => " + tools.ft_ftoa(b) +"x + " + tools.ft_ftoa(c) +" = 0\n[Verbose] x = -c / b => x = -" + tools.ft_ftoa(c) + " / " + tools.ft_ftoa(b))
        print("The solution is:")
        print(str(-c/b))

def degree_two(polynomes) :
    print("Polynomial degree: 2")
    a = 1
    b = 1
    c = 1
    if 2 in polynomes :
        a = polynomes[2]
    if 1 in polynomes :
        b = polynomes[1]
    if 0 in polynomes :
        c = polynomes[0]
    v.verbose('Discriminant formule: b^2 - 4ac')
    v.verbose('Discriminant equation: ' +  str(b) + '^2 - 4 * ' + str(a) + ' * ' + str(c))
    discriminant = (b * b) - 4 * a * c
    v.verbose('Discriminant : ' + str(discriminant))
    if discriminant < 0 :
        print('Discriminant is strictly negatif, there is no solution.')
        sys.exit()
    if discriminant == 0 :
        print('Discriminant is equal to zero, there is one solution :')
        v.verbose('Solution formule : x = -b/(2a)')
        v.verbose('Solution equation : x = -' + str(b) + '/ ( 2 * ' + str(a) + ' )') 
        x = (- b) / ( 2 * a)
        print('The solution is :\n', x)
    if discriminant > 0 :
        print('Discriminant is strictly positive, the two solutions are :')
        v.verbose('Solution formules : x1 = (-b-√∆)/(2a) et x2 = (-b+√∆)/(2a)')
        x1 = (- b - (discriminant ** 0.5)) / (2 * a)
        x2 = (- b + (discriminant ** 0.5)) / (2 * a)
        print(x1)
        print(x2)
    
def solver(polynomes, degree):
    if degree == 2 and polynomes[2] != 0:
        degree_two(polynomes)
    elif (degree == 1 or 1 in polynomes) and polynomes[1] != 0:
        degree_one(polynomes)
    elif degree >= 0 and degree <= 2:
        degree_zero(polynomes)
    elif degree > 0:
        print("Polynomial degree: ", degree)
        print ("The polynomial degree is strictly greater than 2, I can't solve.")
    else:
        print("Polynomial degree: ", degree)
        print ("The polynomial degree is negative, I can't solve.")
