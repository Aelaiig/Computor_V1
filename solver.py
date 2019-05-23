import verbose as v

def degree_zero(polynomes):
    print("Polynomial degree: 0")
    ret = polynomes.get(0, 0)
    if ret == 0:
        print ("All reals numbers are a solution for this equation")
    else:
        print("There is no solution for this equation")

def degree_one(polynomes):
        print(polynomes)
        if 1 in polynomes:
            b = polynomes[1]
        else:
            b = 0
        if 0 in polynomes:
            c = polynomes[0]
        else:
            c = 0
        if b == 0 and c == 0:
            print (" 2 All reals numbers are a solution for this equation")
        if b == 0 and c != 0:
            print("2 There is no solution for this equation")

 #       v.verbose("x = -")
def twoDegree(polynomes) :
    print(polynomes)
    
def solver(polynomes, degree):
    if degree == 2 and polynomes[2] != 0:
        twoDegree(polynomes)
    elif (degree == 1 and polynomes[1] != 0) or (1 in polynomes and polynomes[1] != 0):
        degree_one(polynomes)
    elif degree >= 0 and degree <= 2:
        degree_zero(polynomes)
    else:
        print("Polynomial degree: ", degree)
        print ("The polynomial degree is strictly greater than 2, I can't solve.")
