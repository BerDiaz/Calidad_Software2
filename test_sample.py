from app.calculate import nombre_func

def test_vista():
    assert nombre_func(3,4) == 5
    