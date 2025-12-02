from employee_info import get_employees_by_age_range


def test_total_cost_shopping():
    result = []
    test_arr = [{'name': 'Jane', 'age': 25, 'department': 'Marketing', 'salary': 60000}]
    result = get_employees_by_age_range(24, 26)
    assert (result == test_arr)

