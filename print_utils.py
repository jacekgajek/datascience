import IPython.display as dis
import numpy as np

def printmd(expr):
    dis.display(dis.Markdown(r"$$\begin{align}" + expr + r"\end{align}$$"))


def printpol(p):
    def powstr(k):
        if k == 0:
            return ""
        elif k == 1:
            return "z"
        else:
            return "z^" + str(k)

    def op(a):
        if a == 1:
            return ""
        elif a > 0:
            return "+" + str(a)
        else:
            return "-" + str(-a)

    expr = [op(a) + powstr(k) for k, a in enumerate(p[0:len(p)])]
    printmd("s(z)=" + ''.join(np.flip(expr)))
