from exp_decay import ExponentialDecay

def test_ExponentialDecay():
    u = 3.2
    a = 0.4
    utest = -1.28
    e = 1.0 * 10**-14
    f = ExponentialDecay(a)
    ut = f(1,u)
    assert abs(utest - ut) < e, 'PotentialDecay __call__ is wrong.'
test_ExponentialDecay()
