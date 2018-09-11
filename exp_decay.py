import numpy as np
import scipy.integrate as sp
class ExponentialDecay(object):
    """Lalallalalaalaaaa, blablalba, lalaaa"""
    def __init__(self, a):
        self.a = a
    def __call__(self, t, u):
        dudt = -self.a*u
        return(dudt)
    def solve(self, u0, T, dt):
        t = range(0,T+1,dt)
        ut = sp.solve_ivp(dudt,t,t_eval=array_like)
        return(t,ut)

a = 0.4
u0 = [3.2]
T = 5
dt = 101

decay_model = ExponentialDecay(a)
t, u = decay_model.solve(u0, T, dt)

plt.plot(t, u)
plt.show()
