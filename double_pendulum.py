import numpy as np

g = 9.81

class DoublePendulum():
    def __init__(self, M1=1, L1=1, M2=1, L2=1):
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




a = DoublePendulum()
print(a(np.linspace(0,10,101), (1,2,3,4)))
