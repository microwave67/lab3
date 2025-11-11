from lab2.lab2b import find_min_max
from lab2.lab2b import calc_average
from lab2.lab2b import calc_median_temperature

def test_minmax():
    result = []
    input_arr = [3.0, 6.0, 7.0, 8.0, 4.0]
    test_arr = [3.0, 8.0]

    result = find_min_max(input_arr)

    assert (result == test_arr)

def test_avg():
    result = []
    input_arr = [3.0, 7.0, 8.0, 4.0, 5.0]
    test_arr = 5.4

    result = calc_average(input_arr)

    assert (result == test_arr)

def test_median():
    result = []
    input_arr = [3.0, 4.0, 5.0, 7.0, 8.0]
    test_arr = 5.0

    result = calc_median_temperature(input_arr)

    assert (result == test_arr)