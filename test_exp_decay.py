from exp_decay import ExponentialDecay
from numpy import linspace

a = 0.4
u0 = (3.2,)
T = 5
dt = 2

decay_model = ExponentialDecay(a)
t, u = decay_model.solve(u0, T, dt)

plt.plot(t, u)
plt.show()
