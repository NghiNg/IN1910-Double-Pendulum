import scipy.integrate as sp
import numpy as np
import math

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

    def solve(self, y0, T, dt, angles='rad'):
        '''y0 is tuple of (theta0, omega0)
        angles can be 'rad' for radians or 'deg' for degrees.'''
        time = np.linspace(0,T+1,dt)
        if angles == 'deg':
            math.radians(y0[0])
        elif angles == 'rad':
            pass
        else:
            raise NameError('Keyword angles must be rad or deg as string.')
        solution = sp.solve_ivp(self, (0,T+1), y0, t_eval=time)
        t = solution.t
        theta = solution.y
        omega = solution.sol

        def t(self):
            return time
        def theta(self):
            return theta
        def omega(self):
            return omega

        solution = property(t,theta,omega)


a = Pendulum()
a.solve((0,20), 50, 101)
