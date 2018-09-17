import scipy.integrate as sp
import numpy as np
import math

g = 9.81        # gravitational acceleration [m/s**2]

class DoublePendulum():
    def __init__(self, M1=1, L1=1, M2=1, L2=1):
        # mass of pendulum and length of rope for pendulum 1 an 2 respectively
        self.M1, self.M2, self.L1, self. L2 = M1, M2, L1, L2

    def __call__(self, t, y):
        '''
        t: an array of time steps from (0,T)
        y: a tuple of (theta1, omega1, theta2, omega2)
        '''
        M1, M2, L1, L2 = self.M1, self.M2, self.L1, self.L2

        dthetadt1 = y[1]
        dthetadt2 = y[3]

        dtheta = y[0] - y[2]

        domegadt1 = (M2*L1*y[1]**2*np.sin(dtheta)*np.cos(dtheta) + M2*g*np.sin(y[2])*np.cos(dtheta) + M2*L2*y[3]**2*np.sin(dtheta) - (M1 + M2)*g*np.sin(y[0])) / ((M1 + M2)*L1 - M2*L1*np.cos(dtheta)**2)
        domegadt2 = (-M2*L2*y[3]**2*np.sin(dtheta)*np.cos(dtheta) + (M1 + M2)*g*np.sin(y[0])*np.cos(dtheta) - (M1 + M2)*L1*y[1]**2*np.sin(dtheta) - (M1 + M2)*g*np.sin(y[2])) / ((M1 + M2)*L2 - M2*L2*np.cos(dtheta)**2)

        return (dthetadt1, domegadt1, dthetadt2, domegadt2)

    def solve(self, y0, T, dt, angles='rad'):
        '''
        method for solving initial value problem for motion of a single pendulum

        y0:     A tuple of (theta1_0, omega1_0, theta2_0, omega2_0)
        T:      Timespan
        angles: Optional keyword argument, by default 'rad' for radians
                or set to 'deg' for degrees
        '''
        time = np.linspace(0,T+1,dt)

        # determining 'angles'-keyword functionality
        if angles == 'deg':
            math.radians(y0[0])
            math.radians(y0[2])
        elif angles == 'rad':
            pass
        else:
            raise NameError('Keyword angles must be rad or deg as string.')

        solution = sp.solve_ivp(self, (0,T+1), y0, t_eval=time)

        self._t = solution.t
        self._theta1, self._omega1, self._theta2, self._omega2 = solution.y

    @property
    def t(self):
        return self._t
    @property
    def theta1(self):
        return self._theta1
    @property
    def theta2(self):
        return self._theta2
    @property
    def x1(self):
        self._x1 = self.L1*np.sin(theta1)
        return self._x1
    @property
    def y1(self):
        self._y1 = -self.L1*np.cos(theta1)
        return self._y1
    @property
    def x2(self):
        self._x2 = x1 + self.L2*np.sin(theta2)
        return self._x2
    @property
    def y2(self):
        self._y2 = y1 - self.L2*np.cos(theta2)
        return self._y2

a = DoublePendulum()
a.solve((1,1,1,1), 10, 101)
