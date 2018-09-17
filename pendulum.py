#This is for me to do tests of things in.
#For now, I will add changes to things when I work alone and we'll see.

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
        self.solution = sp.solve_ivp(self, (0,T+1), y0, t_eval=time)
        '''self.t = solution.t
        self.theta, self.omega = solution.y'''
        self._t = self.solution.t
        self._theta = self.solution.y[0]
        self._omega = self.solution.y[1]
    @property
    def t(self):
        print('getting value')
        return self._t
    @t.setter
    def t(self,x):
        print('setting value')
        self._t = x
    @property
    def theta(self):
        print('getting value')
        return self._theta
    @theta.setter
    def theta(self,x):
        print('setting value')
        self._theta = x
    @property
    def omega(self):
        print('getting value')
        return self._omega
    @omega.setter
    def omega(self,x):
        print('setting value')
        self._omega = x

    #solution = property(t,theta,omega)
