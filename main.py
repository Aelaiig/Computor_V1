import verbose as verb
import reader as r
import globale as g
import simply as s
import sys

if __name__ == "__main__":
    equation = r.reader(sys.argv)
    simply_form = s.simply(equation)
    print(simply_form)
