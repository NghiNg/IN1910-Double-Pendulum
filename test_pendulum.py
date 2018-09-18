from pendulum import Pendulum
import numpy as np
import nose.tools as nt

y = (np.pi/4, 1)
t = np.linspace(0,100,101)

def test_pendulum1():
    '''
    testing if equations of motion is implemented properly
    '''
    L = 2.2
    ans = -3.15305342
    a = Pendulum(L)
    test = a(t, (np.pi/4, 0.1))
    assert abs(ans - test[1]) < 1e-5, "Pendulum function is wrong."

def test_pendulum2():
    '''
    checking if pendulum with initial conditions at rest stays at rest
    '''
    theta = 0
    omega = 0
    ans = 0
    a = Pendulum()
    test = a(t, (omega, theta))
    assert abs(ans-test[1]) < 1e-10, "Pendulum is not at rest."

def test_radius():
    '''
    testing for a constant rope length
    '''
    a = Pendulum()
    a.solve((0,0.1),10,101)
    r2 = a.x**2 + a.y**2
    assert np.isclose(1**2, np.all(r2))

@nt.raises(ValueError)
def test_solve_called_t():
    a = Pendulum()
    a.t
    a.theta
    a.omega

def test_arrays_zero():
    '''
    test-function for checking if initial conditions y0=(0,0) yields zero-filled arrays
    '''
    a = Pendulum()
    a.solve((0, 0), 10, 1001)
    assert np.all(a.theta == 0) and np.all(a.omega == 0), 'initial conditions \
           y0=(0,0) does not yield arrays with zeros'
