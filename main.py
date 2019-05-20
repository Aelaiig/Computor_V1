import verbose as verb
import reader as r
import globale as g

import sys

if __name__ == "__main__":
    equation = r.reader(sys.argv)
    print(equation , g.verbose)

