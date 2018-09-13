from pendulum import Pendulum
import numpy as np
import nose.tools as nt

y = (np.pi/4, 1)
t = np.linspace(0,100,101)

def test_pendulum1():
    L = 2.2
    ans = -3.153053
    a = Pendulum(L)
    test = a(t, (np.pi/4, 0.1))
    assert abs(ans - test[1]) > 1e-10, "is wrong!!!!!"

test_pendulum1()
