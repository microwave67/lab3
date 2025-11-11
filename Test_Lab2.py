def test_minmax():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 91, 93, 95, 99]
    test_arr = 1

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)