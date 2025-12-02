import employee_info


def test_get_employees_by_age_range():
    result = []
    test_arr = [{'name': 'Jane', 'age': 25, 'department': 'Marketing', 'salary': 60000}]
    result = employee_info.get_employees_by_age_range(24, 26)
    assert (result == test_arr)

def test_calculate_average_salary():
    result = int(employee_info.calculate_average_salary())
    assert (result == 60166)

def test_get_employees_by_dept():
    result = []
    department = "Marketing"
    test_arr = [{'name': 'Jane', 'age': 25, 'department': 'Marketing', 'salary': 60000},{"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}]
    result = employee_info.get_employees_by_dept(department)
    assert (result == test_arr)