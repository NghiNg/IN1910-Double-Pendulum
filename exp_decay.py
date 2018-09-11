import numpy as np
import scipy.integrate as sp

class ExponentialDecay(object):
    """Solves the exponential decay ODE"""
    def __init__(self, a):
        self.a = a
    def __call__(self, t, u):
        dudt = -self.a*u
        return(dudt)
    def solve(self, u0, T, dt):
        t = np.linspace(0,T+1,dt)
        ut = sp.solve_ivp(self, (0,T+1), u0, t_eval=t)
        return(t,ut)
