import scipy as sp
import numpy as np

g = 9.81        # gravitational acceleration [m/s^2]

class Pendulum:
    def __init__(self, L=1, M=1):
        self.L = L      # length of rope [m]
        self.M = M      # mass of pendulum [kg]

    def __call__(self, t, y):
        '''y is a tuple of (theta, omega)'''
        dthetadt = y[1]
        domegadt = -(g/self.L)*np.sin(y[0])
        return(dthetadt, domegadt)
