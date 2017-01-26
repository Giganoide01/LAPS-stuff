from numpy import arange, sin, pi, random, array
import numpy as np
import matplotlib.pyplot as plt
#o = random.random(100)
#x = np.exp(o)
def levenberg(x, y):
    
    #b1, b2, b3, b4, b5 = 10, 1.0 / 3e-2, pi / 6, 8, 7
    #y_true = b1*(0.5 - 1/(1+np.exp(b2*(x -b3)))) + b4*x +b5
    #y_meas = y_true + 2*random.randn(len(x))

    def residuals(p, y, x):
        b1, b2, b3, b4, b5 = p
        err = y - (b1*(0.5 - 1/(1+np.exp(b2*(x -b3)))) + b4*x +b5)
        return err

    def peval(x, p):
        return p[0]*(0.5 - 1/(1+np.exp(p[1]*(x -p[2])))) + p[3]*x +p[4]
    


    p0 = [8, 1 / 2.3e-2, pi / 3, 9, 5]
    #print(array(p0))


    from scipy.optimize import leastsq
    plsq = leastsq(residuals, p0, args=(y, x))
    


    #print(array([b1, b2, b3, b4, b5]))

    t = peval(np.sort(x), plsq[0])
    plt.plot(np.sort(x), t,x,y,'o')
    plt.title('Otimizacao')
    #plt.legend(['Fit', 'Data'])
    return x, t, y, plsq[0]


