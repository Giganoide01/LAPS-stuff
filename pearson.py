import random
import numpy as np

def pearson(x,y):
    
    xb = np.mean(x)
    yb = np.mean(y)

    x1 = xb -x
    
    y1 = yb - y

    a = x1*y1

    num = np.sum(a)

    x2 = x1**2
    y2 = y1**2

    b = np.sum(x2)
    c = np.sum(y2)
    d = c*b
    den = d**0.5

    r = num/den

    return r
