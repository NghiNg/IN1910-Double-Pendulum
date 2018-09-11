from pendulum import Pendulum
import numpy as np
import nose.tools as nt

y = (np.pi/4, 1)
t = np.linspace(0,100,101)

def test_pendulum1():
    L = 2.2
    ans = -0.061122
    a = Pendulum(L)
    test = a(t, (np.pi/4, 0.1))
    nt.assert_equal(test[1], ans)

test_pendulum1()
