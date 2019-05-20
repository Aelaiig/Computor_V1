import sys
import verbose_test as g

def usage():
    print('usage: blabla')
    sys.exit()

def checkArg(argv):
    # global g.verbose
        # if -h usage + exit
    nb_arg = len(sys.argv)
    if nb_arg > 1: 
        if argv[1] == "-h" :
            usage()
        if nb_arg == 3 and argv[2] == "-v":
            g.verbose = 1
        equation = argv[1]
    else :
        usage()
    return equation

def reader(argv):
    result = checkArg(argv)
    # equation = checkSynthax()
    return result

if __name__ == "__main__":
    equation = reader(sys.argv)
    print ('verbose', g.verbose)
    print(equation)