def test_grade():
    grade = 100
    assert grade >= 50

def test_temp():
    temp = float(21)
    f = float((temp * (9/5) + 32))
    convertion = 53
    assert f == convertion

def test_area():
    sidelength = 10
    area = 100  #change this for passed/failed
    assert area == sidelength * sidelength

