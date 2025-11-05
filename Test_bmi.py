from lab2.bmi import calculate_bmi

def test_bmi_normal_weight():
    result = calculate_bmi(weight=57, height=1.73)

    assert (result == 0)

def test_bmi_over_weight():
    result = calculate_bmi(weight=570, height=1.73)

    assert (result == 1)

def test_bmi_under_weight():
    result = calculate_bmi(weight=5, height=1.73)

    assert (result == -1)