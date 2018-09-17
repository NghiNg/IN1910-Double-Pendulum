import nose.tools as nt
from double_pendulum import DoublePendulum
import numpy as np

def test_radius1():
    a = DoublePendulum()
    a.solve((0,0.1, 3,0.5),10,101)
    r2 = a.x1**2 + a.y1**2
    assert np.isclose(1**2, np.all(r2))
test_radius1()

def test_radius2():
    a = DoublePendulum()
    a.solve((0,0.1, 3,0.5),10,101)
    r2 = a.x2**2 + a.y2**2
    assert np.isclose(1**2, np.all(r2))
test_radius2()
