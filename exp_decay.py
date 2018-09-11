import numpy as np
import scipy.integrate as sp

class ExponentialDecay(object):
    """Solves the exponential decay ODE"""
    def __init__(self, a):
        self.a = a
    def __call__(self, t, u):
        dudt = -self.a*u
        print('test')
        return(dudt)
    def solve(self, u0, T, dt):
        #t = np.linspace(0,T+1,dt)
        t = (0,T)
        #u = u0
        #dudt = ExponentialDecay.call(t,u)
        #dudt=call(t,u0)
        print('heihei')
        ut = sp.solve_ivp(dudt,t,u0,t_eval=None)
        return(t,ut)
