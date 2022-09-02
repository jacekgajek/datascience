import IPython.display as dis
import numpy as np


def printlatex(expr):
    dis.display(dis.Markdown(r"$$\begin{align}" + expr + r"\end{align}$$"))


def latex_polynomial(p, varname):
    def powstr(k):
        if k == 0:
            return ""
        elif k == 1:
            return varname
        else:
            return varname + "^" + str(k)

    def op(a):
        if a == 1:
            return ""
        elif a > 0:
            return "+" + str(a)
        else:
            return "-" + str(-a)

    expr = [op(a) + powstr(k) for k, a in enumerate(p[0:len(p)])]
    return ''.join(np.flip(expr))


def latex_matrix(A: np.ndarray):
    expr = r"\begin{bmatrix}"
    n, m = A.shape
    for i in range(0, n):
        # for j in range(0, m):
        expr += "&".join([str(A[i, j]) for j in range(m)]) + r"\\"
    expr += "\end{bmatrix}"
    return expr
