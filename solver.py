import verbose as v
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
        #v.verbose("[Verbose] bx = 0 => "+ tools.ft_ftoa(b) +"x = 0\n[Verbose] x can only be 0")
        print("The solution is:")
        print("0")
    else:
        #v.verbose("[Verbose] bx + c = 0 => " + tools.ft_ftoa(b) +"x + " + tools.ft_ftoa(c) +" = 0\n[Verbose] x = -c / b => x = -" + tools.ft_ftoa(c) + " / " + tools.ft_ftoa(b))
        print("The solution is:")
        print(str(-c/b))

 # v.verbose("x = -")
def twoDegree(polynomes) :
    print(polynomes)
    
def solver(polynomes, degree):
    if degree == 2 and polynomes[2] != 0:
        twoDegree(polynomes)
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
