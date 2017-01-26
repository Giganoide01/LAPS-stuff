import numpy as np
import random
import matplotlib.pyplot as plt
'''
a = 2.0
b = 1
n = 1000
x = np.random.random(n)

y= a*x + b + np.random.random(n)*0.5


#y = np.array([12, 15, 7, 17, 10, 11, 11, 12, 14, 9, 16, 8, 18, 14, 12])

'''
def regressaoLinear(x,y):
    

    XiYi = np.sum(x*y)

    Xi2 = np.sum(x**2)

    Ym =  np.mean(y)

    Xm = np.mean(x)

    n = len(x)
    c = n*Xm*Ym

    b = (XiYi - c)/ (Xi2 - n*(Xm**2))

    a = Ym - b*Xm

    y2 = b*x + a
    
    plt.plot(x, y, 'ro')
    plt.plot(x, y2,'b')
    return b, a
'''
import matplotlib.pyplot as plt
plt.plot(x, y, 'ro')
plt.plot(x, y2,'b')
#plt.axis([-2, 2, -2, 2])
plt.show()
'''
