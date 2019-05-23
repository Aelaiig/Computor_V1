import verbose as v
import sys
import tools


def secondDegree(polynomes) :
    print(polynomes)
    a = 1
    b = 1
    c = 1
    if 2 in polynomes :
        print('polynome 2: ', polynomes[2])
        a = polynomes[2]
    if 1 in polynomes :
        print('polynome 1: ', polynomes[1])
        b = polynomes[1]
    if 0 in polynomes :
        print('polynome 0: ', polynomes[0])
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
    if degree == 0:
        print("degree 0")
    if degree == 1:
        print("degree 1")
    if degree == 2:
        secondDegree(polynomes)
        print("degree 2")
