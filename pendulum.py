import scipy.integrate as sp
import numpy as np
import math
import matplotlib.pyplot as plt

g = 9.81        # gravitational acceleration [m/s^2]

class Pendulum:
    '''
    Class for describing the behaviour of a single pendulum
    '''
    def __init__(self, L=1, M=1):
        self.L = L      # length of rope [m]
        self.M = M      # mass of pendulum [kg]

    def __call__(self, t, y):
        '''
        t: an array of time steps from (0,T)
        y: a tuple of (theta, omega)
        '''
        dthetadt = y[1]                         # time derivative of theta
        domegadt = -(g/self.L)*np.sin(y[0])     # time derivative of omega
        return (dthetadt, domegadt)

    def solve(self, y0, T, dt, angles='rad'):
        '''
        method for solving initial value problem for motion of a single pendulum

        y0:     A tuple of (theta0, omega0)
        T:      Timespan
        angles: Optional keyword argument, by default 'rad' for radians
                or set to 'deg' for degrees
        '''
        time = np.linspace(0,T+1,dt)

        # determining 'angles'-keyword functionality
        if angles == 'deg':
            math.radians(y0[0])
        elif angles == 'rad':
            pass
        else:
            raise NameError('Keyword angles must be rad or deg as string.')

        solution = sp.solve_ivp(self, (0,T+1), y0, t_eval=time)

        self._t = solution.t
        self._theta = solution.y[0]
        #self._omega = solution.y[0]

    # making properties of t, theta, omega, x, y, v, kinetic and potential energy
    @property
    def t(self):
        return self._t
    @t.setter
    def t(self,value):
        self._t = value

    @property
    def theta(self):
        return self._theta
    @theta.setter
    def theta(self,value):
        self._theta = value

    @property
    def omega(self):
        return self._omega
    @omega.setter
    def omega(self,value):
        self._omega = value

    @property
    def x(self):
        self._x = self.L*np.sin(self._theta)
        return self._x

    @property
    def y(self):
        self._y = (-1)*self.L*np.cos(self._theta)
        return self._y

    @property
    def v(self):
        vx = np.gradient(self.x, self.t)
        vy = np.gradient(self.y, self.t)
        self._v = np.asarray([vx, vy])
        return self._v

    @property
    def potential(self):
        self._P = self.M*g*(self.y + self.L)
        return self._P

    @property
    def kinetic(self):
        self._K = 0.5*self.M*(self.v[0]**2 + self.v[1]**2)
        return self._K


class DampenedPendulum(Pendulum):
    '''
    Subclass of Pendulum with updated equations of motion including
    dampening parameter B
    '''
    def __init__(self, L=1, M=1, B=1):
        self.L = L      # lengt of rope [m]
        self.M = M      # mass of pendulum [kg]
        self.B = B      # dampening parameter

    def __call__(self, t, y):
        '''
        t: an array of time steps from (0,T)
        y: a tuple of (theta, omega)
        '''
        dthetadt = y[1]                 # time derivative of theta

        # new time derivative of omega
        domegadt = -(g/self.L)*np.sin(y[0]) - (self.B/self.M)*y[1]
        return (dthetadt, domegadt)

# making Pendulum object a
a = Pendulum()
a.solve((np.pi/4, 0.1), 10, 1001)

# making a DampenedPendulum object b
b = DampenedPendulum(B=0.1)
b.solve((np.pi/4, 0.1), 10, 1001)

# plotting motion of pendulum (theta)
plt.figure('motion')
plt.plot(b.t, b.theta, 'k')

# plotting energy of pendulum (potentibl, kinetic, sum)
plt.figure('energy')
plt.plot(b.t, b.kinetic, color='darkcyan')
plt.plot(b.t, b.potential, color='firebrick')
plt.plot(b.t, b.kinetic + b.potential, color='orange')

plt.show()
