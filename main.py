import verbose as verb
import reader as r
import globale as g
import simply as s
import sys
import tools

if __name__ == "__main__":
    equation = r.reader(sys.argv)
    formatted = tools.simplifier(equation)
    print(formatted)
    simply_form = s.simply(formatted)
    print(simply_form)
